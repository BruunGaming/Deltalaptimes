import datetime
from time import strftime

datetimeFormat = '%M:%S.%f' 

#time1= '1:22.000'
#time2= '2:23.111'

time1 = input()
time2 = input()

diff = datetime.datetime.strptime(time2, datetimeFormat)\
	 - datetime.datetime.strptime(time1, datetimeFormat)

#Interval= datetime.datetime.strptime(diff, datetimeFormat)

print(diff.__format__
	  datetimeFormat)








""" det som næsten virkede
import datetime, time
from time import strftime

datetimeFormat = '%M:%S.%f' 

diff = datetime.datetime.strptime(time2, datetimeFormat)\
 - datetime.datetime.strptime(time1, datetimeFormat)

print(diff)

"""


""" Ting jeg har prøvet


#FormatTime = tistrtime(diff, '%M:%S.%f')
#print ("%M:%S.%f")diff
"""