import time, random
# Must be included in all the scripts 
from locust_plugins.listeners import TimescaleListener 
# Must Import 'events' for script to report metrics to timescale-db
from locust import HttpUser, TaskSet, task, between, events


class MyWebsiteUser(HttpUser):
    wait_time = between(1, 2)

    # Failed transaction to show failures reported in Grafana
    @task
    def index(self):
        self.client.post("/authentication/1.0/getResults", {"postgres": "admin"})

    @task
    def view_art_home_page(self):
        self.client.get("/")

    @task
    def view_art_docs_page(self):
        self.client.get("/docs/guides/overview/welcome.html#Stay-in-touch")

    @task
    def view_art_resources_page(self):
        self.client.get("/docs/resources/index.html#Artillery-Pro")

    @task
    def view_art_pro_page(self):
        self.client.get("/pro")


# Must be added to Locustfile to report execution metrics to timescale
# Grafana Dashboard key to view execution specific data is based on the 'testplan' value
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    TimescaleListener(env=environment, testplan="taurus_art_listener_ex", target_env="myTestEnv")