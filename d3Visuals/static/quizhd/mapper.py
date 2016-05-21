#!/usr/bin/env python

import sys


def getmonth_column(month):
        if month == 'jan':
                return 8
        elif month == 'feb':
                return 10
        elif month == 'mar':
                return 12
        elif month == 'apr':
                return 14
        elif month == 'may':
                return 16
        elif month == 'jun':
                return 18
        elif month == 'jul':
                return 20
        elif month == 'aug':
                return 22
        elif month == 'sept':
                return 24
        elif month == 'oct':
                return 26
        elif month == 'nov':
                return 28
        else:
                return 30
	
def find_count_month(upward,lower,month):
	countabove = 0
	countbelow = 0
	FistLine = True
	for line in sys.stdin:
		if FistLine:
			FistLine = False
			continue
                line = line.strip()
                data = line.split("\n")
                for ln in data:
			columns = ln.split("\",\"")
			cmonth = getmonth_column(month)
			data = float(columns[cmonth])
			if upward - data < 0:
				countabove+=1
			elif lower - data < 0:
				countbelow+=1
                        else:
				pass
	return countabove, countbelow
				
if __name__ == '__main__':
	flag = sys.argv[1]
	upward = float(sys.argv[2])
	lower = float(sys.argv[3])
	month = sys.argv[4]
	if flag == 'p':
		cntabove,cntbelow  = find_count_month(upward,lower, month)
		print ("%d\t%d" %(cntabove,cntbelow))
	else:
		print ("%s\t%f" %("None",0.0))

