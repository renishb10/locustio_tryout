activeUserToken = None

def isAuthenticated():
    if activeUserToken is None:
        return False
    return True

class Report(object):
    def __init__(self, method="", name="", url="", requests=0, failures=0, median_response_tm=0, avg_response_tm=0, min_response_tm=0, max_response_tm=0, avg_content_size=0, req_per_second=0.00):
        self.method = method
        self.name = name
        self.url = url
        self.requests = requests
        self.failures = failures
        self.median_response_tm = median_response_tm
        self.avg_response_tm = avg_response_tm
        self.min_response_tm = min_response_tm
        self.max_response_tm = max_response_tm
        self.avg_content_size = avg_content_size
        self.req_per_second = req_per_second
