#!/usr/bin/env python

from flask import Flask
from nvd3 import discreteBarChart
from nvd3 import scatterChart, lineChart
from flask import render_template,request
import os
import random
from datetime import datetime
import time
import os.path
import subprocess
import socket

app = Flask(__name__)

def socket_connection(host_ip,port,command):
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error:
		sys.exit()
	
	s.connect((host_ip,port))
	try:
		s.sendall(command)
	except socket.error:
		sys.exit()
	reply = s.recv(4096)
	return reply
	

@app.route('/country', methods=['GET','POST'])
def country_selection():
	if request.method == 'POST':
		countryname = request.form['country_name']
		command = 'country' + ',' + countryname
		data = socket_connection('127.0.0.1',7000,command)
		return data
		#os.system("/var/www/html/assignment5/launch_hdp.sh" + " " + str(countryname))	
		
		#process=subprocess.Popen("/var/www/html/assignment5/launch_hdp.sh" + " " + str(countryname),shell=False, stderr=subprocess.PIPE,stdout=subprocess.PIPE)
		#return process.communicate()


@app.route('/multiple',methods=['GET','POST'])
def multiple_selection():
	if request.method == 'POST':
		mappers = request.form['mapper_number']
		reducers = request.form['reducer_number']
		command = 'station' + ',' + mappers + ',' + reducers
		data = socket_connection('127.0.0.1',7000,command)
		return data

def read_data(filepath):
        with open(filepath,'rb') as fileobj:
                content = fileobj.read()
                con = []
                try:
                        lines = content.split("\n")
                        flag = True
                        for ln in lines:
                                if flag:
                                        flag=False
                                        continue
                                columns = ln.split(",")
                                #print columns
                                con.append(columns)
                except:
                       print 'Error'
        return con


def validate_data(content):
        ydata = []
        station = []
        for columns in content:
                try:
                        station.append(columns[1])
                        data = []
                        for it in range(2,26):
                                try:
                                        columns[it] = float(columns[it])
                                        data.append(columns[it])
                                except:
                                        continue
                        ydata.append(data)
                except:
                        continue
        return station,ydata
						
@app.route('/scatter')
def scatter_plot():
	content = read_data('/var/www/html/assignment5/static/dataset_chart1.csv')
        station, ydata = validate_data(content)
	kwargs1 = {'shape': 'circle', 'size': '1','margin_top': 100}
	chart = scatterChart(name='scatterChart', height=1800, width=1800, margin_bottom=200, margin_top=40, margin_left=60, margin_right=10)
        xdata = list(range(1,13))
        for it in range(0,len(station)-1):
                chart.add_serie(y=ydata[it],x=xdata,name=station[it],**kwargs1)
        chart.buildhtml()
        return chart.htmlcontent


@app.route('/barchart')
def bar_chart():
	content = read_data('/var/www/html/assignment5/static/dataset_chart1.csv')
        station, ydata = validate_data(content)
	chart = discreteBarChart(name='discreteBarChart', height=800, width=1800,margin_top=30, margin_bottom=200, margin_left=60, margin_right=10)
	xdata = str("january,feburary,march,april,may,june,july,august,september,outober,november,december").split(",")
	for it in range(0,1):
		chart.add_serie(y=ydata[it],x=xdata,name=station[it])
	chart.buildhtml()
	return chart.htmlcontent	

@app.route('/linechart')
def line_chart():
 	content = read_data('/var/www/html/assignment5/static/dataset_chart1.csv')
	station, ydata = validate_data(content)
	kwargs1 = {'height':'3000'}
	chart = lineChart(name="lineChart",height=900,width=1800,margin_bottom=20, margin_top=40, margin_left=60, margin_right=10)
	xdata = list(range(1,13))
	for it in range(0, len(station)-1):
		chart.add_serie(y=ydata[it],x=xdata,name=station[it])	
	chart.buildhtml()
	return chart.htmlcontent
	#return render_template('test1.html')
		

@app.route('/')
def main_page():
	return render_template('main_page.html')
	
if __name__ == '__main__':
	app.run(debug=True)
