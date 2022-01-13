from server import app


def test_connection_with_unregistered_email():
    response = app.test_client().post('/show_summary', data=dict(email='test@test.com', ))
    assert "Sorry, that email is not registered." in str(response.data)
    assert response.status_code == 200


def test_connection_with_registered_email():
    response = app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    assert "Sorry, that email is not registered." not in str(response.data)
    assert response.status_code == 200
    assert 'Welcome, john@simplylift.co' in str(response.data)


def test_logout():
    app.test_client().get('/show_summary')
    response = app.test_client().get('/logout')
    assert response.status_code == 302


def test_points_display():
    response = app.test_client().get('/points')
    assert response.status_code == 200
    assert 'Simply Lift' in str(response.data)