import time
t1 = time.perf_counter()
def binarySearch(list, item):
	    first = 0
	    last = len(list)-1
	    
	
	    while (first!=last+1):
	        midpoint = (first + last)//2
	        if list[midpoint] > item:
	        	last=midpoint-1
	        elif list[midpoint]<item:
	            first = midpoint+1
	        elif list[midpoint]==item:
	            return midpoint+1
	        else:
	        	return -1
list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
item = 6
print(binarySearch(list,item))
t2 = time.perf_counter()
print (t2-t1)