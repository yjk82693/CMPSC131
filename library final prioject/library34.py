import init as init

# Get the end of the log date
end_of_the_log = init.getLogDate()


def ratiotest(Book):
    # library 3
    book = []
    copies = []

    # book = [Book title]
    # copies = [Copies of books]

    for i in range(len(Book)):
        t = list(Book[i])
        book.append(t[0])
        copies.append(t[1])
    #Total Availability  
    availability = []
    for i in range(copies):
        if len(list(copies[i]))==1:
            n = "endlog"
            availability.append(n)
        else:
            dates = list(copies[i])
            dateofcopy = list(dates[i])
            copies.append(["endlog",list(list(copies[len(copies-1)]))[1]])
            change=0
            for j in range(len(copies)-1):
                x = (list(copies[j+1])[0] - list(copies[j])[0])*dateofcopy[0]
                change+=x
            availability.append(change)
    # total amount of rent
    Rentdaydata = []
    Rentdays = list(Book[3])
    for i in range(len(Rentdays)):
        for j in range(len(RD)):
            sum = 0
            RD = list(Rentdays[j])
            min = RD[0]
            max = RD[1]
            range = max-min+1
            sum += range
        Rentdaydata.append(sum)
    # Calcularing Rate
    rate = []
    for j in range(len(book)):
        r = Rentdaydata[j]/availability[j]
        r.append(rate)
    # Creating 2D List (Book name / Rates)
    bookratio = []
    for k in range(len(book)):
        x = []
        x.append(book[k])
        x.append(rate[k])
        bookratio.append(x)
    # [
    #    [book name / ratio]
    #    .
    #    .
    #    .
    # ]