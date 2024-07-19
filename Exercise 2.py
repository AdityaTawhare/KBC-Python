# Creat a python program capable of greeting you with Good moring, Good Afternoon 
# and Good Evening.Your program should us etime module to get the current hour. 
# Here is a sample program and documentation link for you.

import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the hour:"))
print(hour)

if(hour>0 and hour<12):
    print("Good Moring Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
    print("Good Night Sir!")
