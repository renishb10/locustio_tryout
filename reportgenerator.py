from utilities import csvhelper, sendemail, config
import numpy
from bokeh.layouts import row
from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.plotting import figure, show, output_file
from bokeh.io import export_png
from selenium import webdriver

reader = csvhelper.CsvHelper()
data = reader.readfile()

class ReportGenerator:
    def generateBulletChart(self):
        reportData = self.filterData(data)
        y_requests = self.getRequestsFromData(reportData)
        x_responseTime = self.getResponseTimeFromData(reportData)
        max_avg_responseTime = int(max(x_responseTime)) + 1000

        dot = figure(title="Reach Perfomance Test", tools="", toolbar_location=None,
                    y_range=y_requests, x_range=[10,max_avg_responseTime],
                    x_axis_label='Response time (ms)', y_axis_label='Requests',
                    plot_width=900, plot_height=600)

        dot.segment(0, y_requests, x_responseTime, y_requests, line_width=7, line_color="#5b9aff", )
        dot.circle(x_responseTime, y_requests, size=30, fill_color="orange", line_color="#5b9aff", line_width=9 )

        output_file("reports/outputs/reachperftest.html", title="Reach Performance Test")
        export_png(dot, filename="reports/outputs/reachperftest.png")

        #html = file_html(dot, CDN, "Reach Performance Test")
        #print(html)
        html = '<!DOCTYPE html><html><body><h1>My first SVG</h1><img src="https://akedge.globalenglish.com/9/themes/edge/images/GE2_logo.png"></body></html>'
        email = sendemail.SendEmail()
        email.Send(config.TO_EMAIL_ADDRESSES, html)
        show(dot)  # open a browser

    def getRequestsFromData(self, filteredData):
        requests = []
        for datum in filteredData:
            requests.append(datum["requestName"])
        return requests

    def getResponseTimeFromData(self, filteredData):
        response_time = []
        for datum in filteredData:
            response_time.append(datum["responseTime"])
        return response_time

    def filterData(self, data):
        results = []

        if len(data) > 0:
            for datum in data:
                print(datum.avg_response_tm)
                if datum.name != "Total":
                    results.append({"requestName": datum.name, "responseTime": datum.avg_response_tm})
        
        return results


rep = ReportGenerator()
rep.generateBulletChart()
