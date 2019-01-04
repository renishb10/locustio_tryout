from locust import TaskSet, task
from utilities import helper, config
import json

class LSTasks(TaskSet):

    @task(4)
    def GetMissions(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "missions"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)

    @task(4)
    def GetMissionById(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "missions/" + config.TESTMISSION
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)

    @task(4)
    def GetUserResults(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "users/results"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)

    @task(4)
    def GetUserProgress(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "users/progress"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)

    @task(4)
    def GetUserEncouragements(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "users/encouragements"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)

    @task(4)
    def GetUserTrophies(self):
        if helper.activeUserToken is not None:
            config.LSHEADER["Authorization"] = helper.activeUserToken
            URL = config.LSURL + "users/trophies"
            with self.client.get(URL, headers=config.LSHEADER, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(response.reason)