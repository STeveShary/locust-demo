from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/")

    @task
    def get_all(self):
        self.client.get("/books")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000