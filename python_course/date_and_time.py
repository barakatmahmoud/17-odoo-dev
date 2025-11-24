###
#
#
# Date and Time
#
#
###
import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

####**** Print current Date and Time *****#####
print(datetime.datetime.now())
####**** Print current Year*****#####
print(datetime.datetime.now().year)
####**** Print current Month*****#####
print(datetime.datetime.now().month)
####**** Print current Day*****#####
print(datetime.datetime.now().day)
####**** Print current Time*****#####
print(datetime.datetime.now().time())
####**** Print current Time Hour*****#####
print(datetime.datetime.now().time().hour)
####**** Print current Time Minute*****#####
print(datetime.datetime.now().time().minute)
####**** Print current Time Second*****#####
print(datetime.datetime.now().time().second)
####**** Print Start and End Time*****#####
print(datetime.time.min)
print(datetime.time.max)

