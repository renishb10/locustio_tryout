from locust import TaskSet, task
from utilities import helper, config
import json

class PSTasks(TaskSet):

    @task(2)
    def GetUserTrophies(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.PSURL + "users/profiles"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)