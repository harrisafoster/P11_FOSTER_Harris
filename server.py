import json
from flask import Flask, render_template, request, redirect, flash, url_for
import datetime


def load_clubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def load_competitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    """
    Error catching mechanism that fixed the 500 internal server error
    resultant of trying to log in with an unregistered email.
    :return: Redirect to summary or back to log in
    """
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash('Sorry, that email is not registered.')
        return render_template('index.html')
    else:
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """
    Determines the availability of an event based on its date before sending the user to the booking page.
    :return: Redirects to booking places for chosen event.
    """
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundCompetition['date'] < str(datetime.date.today()):
        flash("Reservations for that event have closed.")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    elif foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub, competitions=competitions)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    """
    Checks the number of intended places against the maximum of 12
    Checks the point cost of the intended reservation against the point total of the user
    Multiplies the intended reservation by 3 to reflect the 3 points per place cost
    :return: Redirects after reservation is made or redirects back to booking page if a condition is not met
    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    club_points = int(club['points'])
    if (placesRequired * 3) > club_points:
        flash('You do not have enough points.')
        flash(f'Points available: {club_points}')
        flash('Remember: one place costs 3 points.')
        return render_template('booking.html', club=club, competition=competition)
    elif placesRequired <= 12:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        club['points'] = int(club['points']) - (placesRequired * 3)
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash('You cannot book more than 12 places.')
        return render_template('booking.html', club=club, competition=competition)


@app.route('/points')
def show_clubs():
    return render_template('points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
