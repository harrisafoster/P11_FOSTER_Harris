from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.post("/show_summary", {
            "email": "admin@irontemple.com",
        })

    @task
    def index(self):
        self.client.get("/book/Fall%20Classic/Iron%20Temple")

    @task
    def about(self):
        self.client.get("/")

    @task
    def logout(self):
        self.client.get('/logout')

    @task
    def purchase(self):
        self.client.post('/purchase_places', {
            'places': '10',
            'competition': 'Fall Classic',
            'club': 'Iron Temple',
        })

    @task
    def points(self):
        self.client.get('/points')
