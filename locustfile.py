import time, random
from locust import HttpUser, TaskSet, task, between 


class MyWebsiteUser(HttpUser):
    wait_time = between(1, 2)

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
