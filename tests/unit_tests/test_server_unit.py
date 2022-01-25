from server import app


def test_connection_with_unregistered_email():
    """
    Attempts to log in with an registered email.
    :return: Passed if application notifies the user that the email is not registered and then allows the user
    to try logging in again
    Failed if an error occurs (internal server)
    """
    response = app.test_client().post('/show_summary', data=dict(email='test@test.com', ))
    assert "Sorry, that email is not registered." in str(response.data)
    assert response.status_code == 200


def test_connection_with_registered_email():
    """
    Attempts to log in with a registered email.
    :return: Passed if connection is established. Failed if connection fails.
    """
    response = app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    assert "Sorry, that email is not registered." not in str(response.data)
    assert response.status_code == 200
    assert 'Welcome, john@simplylift.co' in str(response.data)


def test_logout():
    """
    Attempts to log out of the application
    :return: Passed if logout is successful. Failed if an error occurs or logout is unsuccessful.
    """
    app.test_client().get('/show_summary')
    response = app.test_client().get('/logout')
    assert response.status_code == 302


def test_points_display():
    """
    Attempts to go to the points display board.
    :return: Failed if page is not displayed. Passed if page is displayed successfully.
    """
    response = app.test_client().get('/points')
    assert response.status_code == 200
    assert 'Simply Lift' in str(response.data)
