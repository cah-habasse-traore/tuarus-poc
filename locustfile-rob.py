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
    def view_rob_home_page(self):
        self.client.get("/")

    @task
    def view_rob_introduction_page(self):
        self.client.get("/#introduction")

    @task
    def view_rob_examples_page(self):
        self.client.get("/#examples")

    @task
    def view_rob_libraries_page(self):
        self.client.get("/#libraries")


# Must be added to Locustfile to report execution metrics to timescale
# Grafana Dashboard key to view execution specific data is based on the 'testplan' value
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    TimescaleListener(env=environment, testplan="taurus_rob_listener_ex", target_env="myTestEnv")