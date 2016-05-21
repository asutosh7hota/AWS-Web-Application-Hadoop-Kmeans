#!/usr/bin/env python

from operator import itemgetter
import sys



def find_max_condition():
	current_station = None
	current_maxvalue = 0
	for line in sys.stdin:
		line = line.strip()
		station, value = line.split('\t',1)
		value = float(value)
		if current_maxvalue - value < 0:
			current_maxvalue = value
			current_station = station
				
	return current_station,current_maxvalue


def find_min_value():
	current_station = None
	current_value = 9999.99
	for line in sys.stdin:
		line = line.strip()
		station, value = line.split('\t',1)
		value = float(value)
		if current_value - value > 0:
			current_value = value
			current_station = station
	return current_station, current_value

if __name__ == '__main__':
	indicator = sys.argv[1]
	if indicator == 'p':
		for line in sys.stdin:
			line = line.strip()
			cntabv,cntbel = line.split('\t',1)
			print ("%s\t%s" %(cntabv,cntbel))

	elif indicator == 'station':
		station_name, value = find_min_value()
		print  ("%s\t%f" %(station_name,value))
	else:
		print ("%s\t%f" %("None",0.0))

