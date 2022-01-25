from server import app


def test_user_cannot_book_more_than_points_available():
    """
    Attempts to use more booking points than available.
    :return: Failed if action is allowed, Passed if action is not allowed.
    """
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=50, competition='Fall Classic', club='Simply Lift'))
    assert "You do not have enough points." in str(response.data)
    assert "Points available: 13" in str(response.data)
    assert response.status_code == 200


def test_user_cannot_book_more_than_12():
    """
    Attempts to book more than 12 places for an event.
    :return: Failed if action is allowed, passed if action is not allowed
    """
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="admin@irontemple.com", ))
    app.test_client().get('/book/Fall%20Classic/Iron%20Temple')
    response = app.test_client().post('/purchase_places',
                                      data=dict(places=13, competition='Fall Classic', club='Iron Temple'))
    assert "You cannot book more than 12 places." in str(response.data)
    assert response.status_code == 200


def test_point_changes_are_reflected():
    """
    Attempts to book places in a competition using points.
    :return: Failed if points are not deducted from the user's total, passed if the points are deducted from the
    user's total
    """
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=12,
                                                                    competition='Fall Classic',
                                                                    club='Simply Lift'))
    assert b'Points available: 1' in response.data
    assert response.status_code == 200


def test_user_cannot_book_past_event():
    """
    Attempts to book an event that has already begun.
    :return: Failed if action is allowed. Passed if action is not allowed.
    """
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    response = app.test_client().get('/book/Spring%20Festival/Simply%20Lift')
    assert b'How many places?' not in response.data
    assert b'Reservations for that event have closed.' in response.data
    assert response.status_code != 500


def test_one_place_costs_3():
    """
    Attempts to book places in a competition.
    :return: Passed if one place costs 3 points and those points are deducted from the user's total.
    Failed if the place cost less than 3 points or the points have not been deducted.
    """
    app.test_client().get('/')
    app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    app.test_client().get('/book/Fall%20Classic/Simply%20Lift')
    response = app.test_client().post('/purchase_places', data=dict(places=4,
                                                                    competition='Fall Classic',
                                                                    club='Simply Lift'))
    assert b'Points available: 1' in response.data
    assert response.status_code == 200
