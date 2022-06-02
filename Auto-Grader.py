"""
DataType
<name>, <hw1 grade>, <hw2 grade>, <hw3 grade>, <test1 grade>, <test 2 grade>, <test3 grade>, <test 4 grade>, <project grade>

From this information your program should be able to do the following: 

1) Calculate each student's overall score. (hws are 40%, tests are 40%, project is 20%) without dropping the lowest test grade (Test file usage)

2) Calculate each student's overall score with dropping the lowest test grade while calculating overall score 

3) Your program should be able to find the student with the highest test score, project score and homework score.
Have functions called get_highesttest , get_higestproject etc which return the students name
(these functions can be passed either the filename or a list of student names, approrpiate scores if your solution involves making lists containing the file information)

4) Your program should be able to output how many As, A-s, Bs etc in the class
(you may use the same criteria in the syllabus).
Have a function which you call which outputs the numbers of A,A-s, Bs etc to the screen.
(these functions can be passed either the filename or a list of overall scores if your solution involves making lists containing the file information)
"""


# uin
def addData(inpt, dest):
    single = []
    for i in range(len(inpt)):
        if i == 0:
            single.append(inpt[i].strip())
        else:
            single.append(float(inpt[i].strip()))
    dest.append(single)
    return dest


def uin():
    info = open("info.txt", 'r')
    data = []
    line = info.readline()
    data = addData(line.split(','), data)
    while line != "":
        line = info.readline()
        if line == '':
            continue
        data = addData(line.split(','), data)
    return data


# Get the row with selected student name
def get_row(data, student):
    for i in range(len(data)):
        if data[i][0] == student:
            output = data[i]
    return output


# Calculate the score after dropping the minimum score
def drop_minimum(data):
    return (sum(data)-min(data))*0.4


# Calculate each student's overall score
def get_overall(data, student, drop_min):
    record = get_row(data, student)
    hw_scr = sum(record[1:3])*0.4
    if drop_min:
        ts_scr = drop_minimum(record[4:7])
    else:
        ts_scr = sum(record[4:7])*0.4
    fn_scr = record[-1]*0.2
    return hw_scr+ts_scr+fn_scr


# Get the student with highest test score
def get_highestTest(data):
    maximum = sum(data[0][4:7])
    maxname = data[0][0]
    for i in range(1, len(data)):
        if sum(data[i][4:7]) > maximum:
            maximum = sum(data[i][4:7])
            maxname = data[i][0]
    return maxname


# Get the student with highest homework score
def get_highestHomework(data):
    maximum = sum(data[0][1:3])
    maxname = data[0][0]
    for i in range(1, len(data)):
        if sum(data[i][1:3]) > maximum:
            maximum = sum(data[i][1:3])
            maxname = data[i][0]
    return maxname


# Get the student with highest project score
def get_highestProject(data):
    maximum = data[0][-1]
    maxname = data[0][0]
    for i in range(1, len(data)):
        if data[i][-1] > maximum:
            maximum = data[i][-1]
            maxname = data[i][0]
    return maxname


# Get the letter grade
def get_letterGrade(data):
    LetterGrade = [0, 0, 0, 0, 0, 0, 0, 0]
    for row in data:
        score = get_overall(data, row[0], False)
        if score >= 92.5:
            LetterGrade[0] += 1
        elif score >= 88.5:
            LetterGrade[1] += 1
        elif score >= 83.5:
            LetterGrade[2] += 1
        elif score >= 79.5:
            LetterGrade[3] += 1
        elif score >= 76.5:
            LetterGrade[4] += 1
        elif score >= 69.5:
            LetterGrade[5] += 1
        elif score >= 59.5:
            LetterGrade[6] += 1
        else:
            LetterGrade[7] += 1
    print("A:", LetterGrade[0])
    print("A-:", LetterGrade[1])
    print("B+:", LetterGrade[2])
    print("B:", LetterGrade[3])
    print("B-:", LetterGrade[4])
    print("C+:", LetterGrade[5])
    print("C:", LetterGrade[6])
    print("F:", LetterGrade[7])


