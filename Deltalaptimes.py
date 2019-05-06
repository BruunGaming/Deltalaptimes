import datetime
from datetime import timedelta

datetimeFormat = '%M:%S.%f' 

time1 = '1:22.000'
time2 = '2:23.111'




diff = datetime.datetime.strptime(time2, datetimeFormat)\
	 - datetime.datetime.strptime(time1, datetimeFormat)


print(diff)

