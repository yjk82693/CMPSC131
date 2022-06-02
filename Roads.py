#Getting inputs
roads = []
n = int(input("Enter numbers of road: "))
for l in range(n):
    rd = input("Road name: ")
    roads.append(rd)
start = input("Enter starting city: ")
destination = input("Enter destination city: ")

result = False
#Seperating destination and starting point
st=[]
dt=[]
for m in range(len(roads)):
    rd = roads[m]
    alst = rd.split('-')
    st.append(alst[0])
    dt.append(alst[1])
#Availability checking
#if start matches one of element in st, and destination matches one of element in dt, it matches
i=0
while(i<len(roads)):
    j=i+1
    while(j<len(roads)):
        k=i+1
        while(k<len(roads)):
            #destination matches
            if(st[i]==start or st[j]==start or st[k]==start):
                if(dt[i]==destination or dt[j]==destination or dt[k]==destination):
                    result = True
            k+=1
        j+=1
    i+=1

if(result == True):
    print("Yes, it is possible to go from starting city to the destination city using 3 or fewer roads.")
else:
    print("No, it is impossible to go from starting city to the destination city using 3 or fewer roads.")
