from server import app


def test_not_enough_points():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=50, competition='Fall Classic', club='Simply Lift'))
    assert "You don't have enough points." in str(response.data)
    assert "Points available: 13" in str(response.data)


def test_overbook():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=13, competition='Fall Classic', club='Simply Lift'))
    assert "You cannot book more than 12 places." in str(response.data)


def test_point_change_reflection():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=12, competition='Fall Classic', club='Simply Lift'))
    assert b'Points available: 13' not in response.data


def test_book_past_event():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    response = app.test_client().get('/book/Spring%20Festival/Simply%20Lift')
    assert b'How many places?' not in response.data