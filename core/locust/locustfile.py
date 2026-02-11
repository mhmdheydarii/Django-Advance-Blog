from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post("/accounts/api/v1/jwt/login/", data={
            "email":"mohammad@gmail.com",
            "password":"1234"
        }).json()

        self.client.headers = {'Authorization': f'Bearer {response.get("access", None)}'}


    @task
    def get_post(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def get_category(self):
        self.client.get("/blog/api/v1/category/")