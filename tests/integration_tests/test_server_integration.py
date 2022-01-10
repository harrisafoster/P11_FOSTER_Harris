from server import app


def test_not_enough_points():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=50, competition='Fall Classic', club='Simply Lift'))
    assert "Too many points" in str(response.data)
    assert "Points available: 13" in str(response.data)


def test_overbook():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=13, competition='Fall Classic', club='Simply Lift'))
    assert "Clubs cannot reserve more than 12 places per competition" in str(response.data)


def test_point_change_reflection():
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=11, competition='Fall Classic', club='Simply Lift'))
    assert "Points available: 1" in str(response.data)