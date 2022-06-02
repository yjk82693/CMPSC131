def upDown(n):
    for i in range(0,len(str(n))-1):
        if str(n)[i]<=str(n)[i+1]:
            return "Up Number"
        elif str(n)[j]>=str(n)[j+1]:
            return "Down Number"
        else:
            return "Neither"
