from server import app


def test_user_cannot_book_more_than_points_available():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=50, competition='Fall Classic', club='Simply Lift'))
    assert "You do not have enough points." in str(response.data)
    assert "Points available: 13" in str(response.data)
    assert response.status_code == 200


def test_user_cannot_book_more_than_12():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=13, competition='Fall Classic', club='Simply Lift'))
    assert "You cannot book more than 12 places." in str(response.data)
    assert response.status_code == 200


def test_point_changes_are_reflected():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=12, competition='Fall Classic', club='Simply Lift'))
    assert b'Points available: 1' in response.data
    assert response.status_code == 200


def test_user_cannot_book_past_event():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    response = app.test_client().get('/book/Spring%20Festival/Simply%20Lift')
    assert b'How many places?' not in response.data
    assert response.status_code != 500


def test_one_place_costs_3():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=4, competition='Fall Classic', club='Simply Lift'))
    assert b'Points available: 1' in response.data
    assert response.status_code == 200