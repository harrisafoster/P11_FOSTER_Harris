from server import app


def test_connection_invalid():
    response = app.test_client().post('/show_summary', data=dict(email='test@test.com', ))
    assert "Sorry, that email is not registered." in str(response.data)
    assert response.status_code == 200


def test_connection_valid():
    response = app.test_client().post('/show_summary', data=dict(email="john@simplylift.co", ))
    assert not "Sorry, that email is not registered." in str(response.data)
    assert response.status_code == 200
    assert 'Welcome, john@simplylift.co' in str(response.data)


def test_if_finished():
    response = app.test_client().post('/show_summary', data=dict(email="john@simplylift.co"))
    assert ('Competition is finished' in str(response.data) or 'In progress' in str(response.data))


def test_logout():
    app.test_client().get('/show_summary')
    response = app.test_client().get('/logout')
    assert response.status_code == 302