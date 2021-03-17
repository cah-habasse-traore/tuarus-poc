import time, random
from locust import HttpUser, TaskSet, task, between 

auction_num = random.randint(1,300)
print("Random Number", auction_num)

class BrowseSite(TaskSet):
 
    @task
    def view_main_page(self):
        self.client.get("/cgi-bin/mncal.cgi?ccoa")

    @task
    def view_auction_page(self):
        self.client.get("/cgi-bin/mndetails.cgi?ccoa32")

    @task(3)
    def view_all_biditems_page(self):
        self.client.get("/cgi-bin/mnlist.cgi?ccoa"+auction_num+"/category/ALL")

    @task(4)
    def view_biditem_detail_page(self):
        self.client.get("cgi-bin/mnlist.cgi?ccoa"+auction_num+"/1")

class MyWebsiteUser(HttpUser):
    tasks = [BrowseSite]
    host = "https://www.capitalcityonlineauction.com"

    # we assume someone who is browsing the Locust docs,
    # generally has a quite long waiting time (between
    # 20 and 600 seconds), since there's a bunch of text
    # on each page
    wait_time = between(1, 2)