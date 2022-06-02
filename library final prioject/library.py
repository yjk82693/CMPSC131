welcome_msg = "1) Can a student borrow a book on a particular day for a certain number of days?\n 2) What are the most borrowed/popular books in the library?\n 3) Which books have the highest borrow ratio?\n 4) Sorted lists of most borrowed books / books with highest usage ratio.\n 5) What are the pending fines at the end of the log/at a specific day in the log?\n Press any other key to exit\n"


# Construct a dataframe by reading through the booklist
def readBookList():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    booklist = open("booklist.txt", 'r', encoding='utf-8')
    line = booklist.readline()
    addBookInfo(line, dataframe)
    while line != "":
        line = booklist.readline()
        if line != "":
            addBookInfo(line, dataframe)
    booklist.close()
    return dataframe


# Process each line of the list
def addBookInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            pcs.append(int(item))
        # Book Restriction
        elif i == 2:
            if item == "FALSE":
                pcs.append(False)
            elif item == "TRUE":
                pcs.append(True)
            else:
                ValueError
    pcs.append([])
    dest.append(pcs)
    return dest


# Construct another file from the dataframe
def create_Cache_Book(dataframe):
    outputStr = ""
    for line in dataframe:
        linestr = ""
        for i in range(len(line)):
            # Book Name
            if i == 0:
                linestr += line[i]+"#"
            # Total Copies
            if i == 1:
                linestr += str(line[i])+"#"
            # Restriction:
            if i == 2:
                linestr += str(line[i])+"#"
            # Borrow Time
            if i == 3:
                # Iterate through the list
                for timeTuple in line[i]:
                    linestr += str(timeTuple[0])+','+str(timeTuple[1])+';'
        linestr += '\n'
        outputStr += linestr
    cache_book = open("cache_book.txt", 'w', encoding='utf-8')
    cache_book.write(outputStr)
    cache_book.close()


# Read from cache_book.txt and construct a dataframe
def read_Cache_Book():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    cache_book = open("cache_book.txt", 'r', encoding='utf-8')
    line = cache_book.readline()
    getCacheBookInfo(line, dataframe)
    while line != "":
        line = cache_book.readline()
        if line != "":
            getCacheBookInfo(line, dataframe)
    cache_book.close()
    return dataframe


def getCacheBookInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            pcs.append(int(item))
        # Book Restriction
        elif i == 2:
            if item == "False":
                pcs.append(False)
            elif item == "True":
                pcs.append(True)
            else:
                ValueError
        # Borrow Time
        else:
            # item = 1, 7; 2, 5; 1, 10;
            borrowTime = []
            for timeTupleStr in item.split(';'):
                timeTuple = []
                timeTupleList = timeTupleStr.strip().split(',')
                for i in range(len(timeTupleList)):
                    if timeTupleList[i] != "":
                        timeTuple.append(int(timeTupleList[i]))
                if len(timeTuple) != 0:
                    borrowTime.append(timeTuple)
            pcs.append(borrowTime)
    dest.append(pcs)
    return dest


current_booklist = readBookList()
current_booklist[1][3].append([1, 7])
current_booklist[1][3].append([2, 5])
current_booklist[1][3].append([1, 10])
create_Cache_Book(current_booklist)
print(read_Cache_Book())
