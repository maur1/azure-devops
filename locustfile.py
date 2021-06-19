import time
from locust import HttpUser, task, between
import json

class LocustTest(HttpUser):

    wait_time = between(1, 2.5)

    @task(1)
    def get_user_list(self):
        self.client.get("/")
    
    @task(2)
    def get_user_a(self):
        self.client.post("/predict",
        data = json.dumps({  
            "CHAS":{"0":0},
            "RM":{"0":6.575},
            "TAX":{"0":296.0},
            "PTRATIO":{"0":15.3},
            "B":{"0":396.9},
            "LSTAT":{"0":4.98},
            }
        ),
        headers={"Content-Type": "application/json"},)

