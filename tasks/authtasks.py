from locust import TaskSet, task
from utilities import config, helper
import json

class AuthTasks(TaskSet):

    @task(1)
    def GetAuthToken(self):
        URL = config.AUTHURL + "login"
        with self.client.post(URL, data=config.PAYLOAD, headers=config.AUTHHEADER, catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if helper.activeUserToken is None:
                    helper.activeUserToken = "Bearer " + data["access_token"]
                response.success()
            else:
                response.failure(response.reason)