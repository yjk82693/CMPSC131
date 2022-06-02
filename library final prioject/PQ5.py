Pr = open("SampleProfile","w")
Pr.write("Greg Black, 50, 20, 30, 20, 40, 60, 10, 23")
Pr.close()

Pread = open("SampleProfile","r")
s=Pread.readline()

lst = s.split(',')
print(lst)

#HW
hw = []
hsum=0
for i in range(1,4):
    hw.append(lst[i])
    hsum+=int(lst[i])
print(hw)
print(hsum)

#Test
test = []
tsum=0
for j in range(4,8):
    test.append(lst[j])
    tsum+=int(lst[j])
print(test)
print(tsum)

#Final Project
project = []
project.append(lst[8])
print(project)
pscore = int(lst[8])
print(pscore)

#Overall
score = hsum//3*0.4 + tsum//4*0.4 +pscore*0.4
print(score)

#excluding worst score of test
test.sort()
tsum-=int(test[0])
print(tsum)
altered = hsum//3*0.4 + tsum//3*0.4 +pscore
print(altered)

#Grade Determiner
if score >= 92.5:
    print("A")
elif score >= 88.5:
    print("A-")
elif score >= 83.5:
    print("B+")
elif score >= 79.5:
    print("B")
elif score >= 76.5:
    print("B-")
elif score >= 69.5:
    print("C+")
elif score >= 59.5:
    print("C")
else:
    print("F")

#Grade dropping worst score
if altered >= 92.5:
    print("A")
elif altered >= 88.5:
    print("A-")
elif altered >= 83.5:
    print("B+")
elif altered >= 79.5:
    print("B")
elif altered >= 76.5:
    print("B-")
elif altered >= 69.5:
    print("C+")
elif altered >= 59.5:
    print("C")
else:
    print("F")
    
