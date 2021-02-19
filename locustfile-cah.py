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
    def view_home_page(self):
        self.client.get("/en.html")

    @task
    def view_service_page(self):
        self.client.get("/en/services.html")

    @task
    def view_professional_products_page(self):
        self.client.get("/en/product-solutions.html")

    @task
    def view_essential_insights_page(self):
        self.client.get("/en/essential-insights.all_audience.html")


# Must be added to Locustfile to report execution metrics to timescale
# Grafana Dashboard key to view execution specific data is based on the 'testplan' value
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    TimescaleListener(env=environment, testplan="taurus_cah_listener_ex", target_env="myTestEnv")