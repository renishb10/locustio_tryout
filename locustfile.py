from locust import HttpLocust
from tasks import authtasks, pstasks, lstasks
from utilities import helper, config

class IdentityServer(HttpLocust):
    task_set = authtasks.AuthTasks
    min_wait = config.MIN_WAIT
    max_wait = config.MAX_WAIT
    host = config.HOST

class ProgramSolution(HttpLocust):
    task_set = pstasks.PSTasks
    min_wait = config.MIN_WAIT
    max_wait = config.MAX_WAIT
    host = config.HOST

class LearningService(HttpLocust):
    task_set = lstasks.LSTasks
    min_wait = config.MIN_WAIT
    max_wait = config.MAX_WAIT
    host = config.HOST