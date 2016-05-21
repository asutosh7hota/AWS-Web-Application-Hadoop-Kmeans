#!/usr/bin/env python
import os
import socket
import numpy as np
from sklearn.cluster import KMeans
import sys
import pickle
import json
from contextlib import closing

HOST = ''
PORT = 7000

def kmeans(ydata,xdata):
        print "starting kmeans"
	#iterate through the list of values present
	newlist = []

	for it in range(0, len(ydata)-1):
		data = [xdata[it],ydata[it]]
		newlist.append(data)
	X = np.array(newlist)
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_
	print 'Centroids:'	
        print centroids
	print 'labels'
        labels = kmeans.labels_
        return centroids,labels



def socket_create(host,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print 'Socket created'

	try:
		s.bind((host, port))
	except socket.error , msg:
		print 'Bind error: ' + str(msg[0])
		sys.exit()
	print 'Socket bind complete'

	while(1):

		s.listen(10)
		print 'Socket now ready'

		conn, addr = s.accept()
		print 'Connection established'

		#with  closing(conn), closing(conn.makefile()) as file1:	
		file1 = conn.makefile()
		jdata = json.load(file1)
		ydata = jdata['ydata']
		xdata = jdata['xdata']
		centroids, labels = kmeans(ydata,xdata)				
		cdata = centroids.tolist()
		ldata = labels.tolist()
		joutput = json.dumps({'centroids':cdata})
		conn.sendall(joutput)
		conn.sendall()
	conn.close()
	s.close()



socket_create(HOST,PORT)

print 'Success'

