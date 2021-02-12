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
    def view_main_page(self):
        self.client.get("/cgi-bin/mncal.cgi?ccoa")

    @task
    def view_auction_page(self):
        auction_num = str(random.randint(1,300))
        self.client.get("/cgi-bin/mndetails.cgi?ccoa"+ auction_num)

    @task
    def view_all_biditems_page(self):
        auction_num = str(random.randint(1,300))
        self.client.get("/cgi-bin/mnlist.cgi?ccoa"+auction_num+"/category/ALL")

    @task
    def view_biditem_detail_page(self):
        auction_num = str(random.randint(1,300))
        self.client.get("/cgi-bin/mnlist.cgi?ccoa"+auction_num+"/1")


# Must be added to Locustfile to report execution metrics to timescale
# Grafana Dashboard key to view execution specific data is based on the 'testplan' value
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    TimescaleListener(env=environment, testplan="taurus_listener_ex", target_env="myTestEnv")