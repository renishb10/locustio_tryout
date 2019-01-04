import csv
from . import helper, config


class CsvHelper:
    def readfile(self):
        recordslist = []
        with open(config.REPORTFILENAME, 'r') as report:
            reader = csv.DictReader(report)
            for row in reader:
                singlerecord = helper.Report()
                singlerecord.method = row['Method']
                singlerecord.name = self.getNameByUrl(row['Name'])
                singlerecord.url = row['Name']
                singlerecord.requests = row['# requests']
                singlerecord.failures = row['# failures']
                singlerecord.median_response_tm = row['Median response time']
                singlerecord.avg_response_tm = row['Average response time']
                singlerecord.min_response_tm = row['Min response time']
                singlerecord.max_response_tm = row['Max response time']
                singlerecord.avg_content_size = row['Average Content Size']
                singlerecord.req_per_second = row['Requests/s']
                recordslist.append(singlerecord)
        return recordslist

    # For time being - crapy code (Error prone)
    def getNameByUrl(self, url):
        requestName = url
        
        try:
            nameLists = config.NAMEFORREQUESTS
            endpoints = url.split("v2/")
            url = url.split("v2/")[1] if len(endpoints) > 1 else url
            return nameLists[url]
        
        except(KeyError):
            return requestName

        except Exception as ex:
            print(ex)