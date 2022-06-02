'''
e.g
timelist = 11:00am 5:00pm 3:45pm 1:00pm 2:00pm

==> 660, 1020, 945, 780, 840
sort() ==> 660, 780, 840, 945, 1020
time_difference ==> 780-660(-5), 840-780(-5), 945-840(-5), 1020-945(-5)
breaktime = input
if breaktime> any of elements in timedifference: it's impossible
if breaktime<difference ==> possible
'''

#inputs
times=input("Enter times: ")
breaktime = int(input("Break Times: "))
timelist = times.split(' ')
timelist_r=[]

#Changing elements in integer (exact minutes)
for i in range(len(timelist)):
    timestr = timelist[i]
    if timestr[-2:] == 'am':            
    #   remove am
    #   change it to min (60*hr + mins)
        hour = int(timestr[:-2].split(':')[0])
        minute = int(timestr[:-2].split(':')[1])
        if(hour==12):
            hour=0
        timelist_r.append(hour*60+minute)
    if timestr[-2:] == 'pm':
    #   remove pm
    #   add 12 hours 
    # e.g: 1pm ==> 1pm + 12hr (change in min)
        hour = int(timestr[:-2].split(':')[0])+12
        minute = int(timestr[:-2].split(':')[1])
        if(hour==12):
            hour-=12
        timelist_r.append(hour*60+minute)
        
#sort times so that you can see time in order
timelist_r.sort()
    
#Check intervals for each testing time
    
time_difference=[]
for i in range(len(timelist_r)-1):
    x=timelist_r[i+1]-timelist_r[i]-5
    time_difference.append(x)

#if minimum value of time difference > break time, it's possible

def findMinimum(mylist):
    minimum = mylist[0]
    for i in range(1, len(mylist)):
        if(mylist[i]<minimum):
            minimum = mylist[i]
    return minimum

minimum = findMinimum(time_difference)

# compare
if minimum > breaktime:
    print("Possible")
else:
    print("Impossible")
