#!/usr/bin/python

from nvd3 import scatterChart
from sklearn.cluster import KMeans
import socket
import numpy as np
import pickle
import csv
import sys
import math
import datetime


HOST=''
PORT = 7000

INPUT_FILE2 = '/var/www/html/assignment5/static/dataset/quakes.csv'

def read_cluster_data(filepath,hzrow):
        readdata = csv.reader(open(filepath,'rb'),delimiter=',')
        xdata = []
        ydata = []
        firstrow = True
        base = 3
        for row in readdata:
                if firstrow:
                        firstrow = False
                        continue
                try:
			'''
                        if len(xdata) > 500:
                                base = 4
                        row[1] = math.log(int(row[1]), base)
                        row[10] = math.log(float(row[10]),base)
                        xdata.append(row[1])
                        ydata.append(row[10])
			'''
			nr = int(hzrow)
			row[nr] = float(row[nr])
			row[16] = float(row[16])
			xdata.append(row[nr])
			ydata.append(row[16])
                except Exception,e: 
			print str(e)
			print row[nr]
			print row[16]
                        continue
        return xdata , ydata



def socket_create():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)	
	print 'Socket Created'
	try:
		s.bind((HOST,PORT))
	except socket.error, msg:
		print 'Bind error: ' + str(msg[0])
		sys.exit()
	print 'Socket bind complete'

        while(1):

                s.listen(10)
                print 'Socket now ready'

                conn, addr = s.accept()
                print 'Connection established'
		
		result = conn.recv(4096)	
		data = result.split(',')
		c1 = data[0]
		r1 = data[1]
		clusters = int(c1)
		diff1 = datetime.datetime.now()
		xdata , ydata = read_cluster_data(INPUT_FILE2,r1)
		print 'Reading from the file'

		#clusters = 4

		centroids,labels,X = kmeans_fn(xdata,ydata,clusters)
		print 'Calculating the centroids and labels'
		with open('/var/www/html/assignment5/templates/finalt.html','wb') as fld:
                        content = generate_chart(X,centroids,labels,clusters)
                        fld.write(content)
		#print 'Written to a file'
		diff2 = datetime.datetime.now()
                diffvalue = diff2 - diff1
		print 'Response time:= ' + str(diffvalue)
                #conn.sendall('Success')
		conn.sendall(content)
		print 'Sent a success message to the client'
	conn.close()
	s.close()	
		


def kmeans_fn(xdata,ydata,n_cluster):
	newlist = []
	for it in range(0, len(xdata)):
		data = [xdata[it],ydata[it]]
		newlist.append(data)
	X = np.array(newlist)
	kmeans = KMeans(n_clusters=n_cluster)
	kmeans.fit(X)

	centroids = kmeans.cluster_centers_
	labels = kmeans.labels_
	return centroids,labels,X

def generate_chart(X,centroids,labels,n_cluster):
	chart = scatterChart(name='scatterChart', height=800, width=1400)

	centxlist = []
	centylist = []
	for i in range(n_cluster):
		newxlist = []
		newylist = []
		centylist.append(newxlist)
		centxlist.append(newylist)
	
	for i in range(len(X)):
		centxlist[labels[i]].append(X[i][0])
		centylist[labels[i]].append(X[i][1])

	
	kwargs1 = {'shape': 'circle', 'size': '1'}
	kwargs2 = {'shape': 'cross', 'size': '5'}
	for i in range(n_cluster):
		chart.add_serie(name="Centroid_" + str(i), y=centylist[i], x=centxlist[i],**kwargs1)
	chart.add_serie(name="Centroids", y=centroids[:,1],x=centroids[:,0],**kwargs2)
	chart.buildhtml()
	return chart.htmlcontent
			
	

if __name__ == "__main__":
	conn = socket_create()

	
	

