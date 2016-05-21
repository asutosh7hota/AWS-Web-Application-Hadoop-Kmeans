#!/usr/bin/env python

import sys
#arg1 = sys.argv[1]
#arg2 = sys.argv[2]
INVALID = -9999

def find_worst_condition(country_name):
	current_station = None
	maxvalue = 0.0
	for line in sys.stdin:
		line = line.strip()
		data = line.split("\n")
		for ln in data:
			try:
				columns = ln.split("\",\"")
				cntry_name = columns[0].strip("\"")
				station_name = columns[1]
				annual = columns[34]
				annual = float(annual)
				if abs(int(annual) - INVALID) == 0:
					continue	
				if cntry_name.lower() == country_name.lower():
					#print ("%s\t%f" %(station_name,annual))
					#print annual
					if maxvalue - annual < 0:
						maxvalue = annual
						current_station = station_name
			except:
				pass
	return current_station, maxvalue		


def find_min_rainfall():
	current_station = None
	minvalue = 9999.99
	for line in sys.stdin:
                line = line.strip()
                data = line.split("\n")
                for ln in data:
                        try:
                                columns = ln.split("\",\"")
                                station_name = columns[1]
                                annual = columns[34]
                                annual = float(annual)
				if abs(int(annual) - INVALID) == 0:
                                        continue
				if minvalue - annual > 0:
					minvalue = annual
					current_station = station_name
			except:
				pass
	return current_station,minvalue	

if __name__ == '__main__':
	flag = sys.argv[1]
	value = sys.argv[2]
	if flag == 'country':
		station_name, maxvalue = find_worst_condition(value)
		print ("%s\t%f" %(station_name,maxvalue))
	elif flag == 'station':
		station_name, minvalue = find_min_rainfall()
		print ("%s\t%f" %(station_name,minvalue))
	else:
		print ("%s\t%f" %("None",0.0))

