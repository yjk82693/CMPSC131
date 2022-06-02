# SSN = XXX-XX-XXXX
from os import read


n = [48, 57]
s = [45, 45]
pattern = [n, n, n, s, n, n, s, n, n, n, n]


def reader():
    fread = open("info.txt", "r")
    line = fread.readline()
    body = line.strip()
    while line != "":
        line = fread.readline()
        body += line.strip()
    fread.close()
    return body


def checker(substring):
    isMatch = True
    # Processing
    for i in range(len(substring)):
        character = substring[i]
        ptn_h = pattern[i][1]
        ptn_l = pattern[i][0]
        if ptn_l > ord(character) or ord(character) > ptn_h:
            # Character matches with pattern at index of i
            return False
    return isMatch


def searcher(body):
    ssn = []
    # Starting index of substring length of 9
    n = 0
    while n+11 <= len(body):
        substring = body[n:n+11]
        # Compare substring with pattern
        doesMatch = checker(substring)
        if doesMatch:
            ssn.append(substring)
        n += 1
    return ssn


def main():
    body = reader()
    ssn = searcher(body)
    fwrite = open("ssninfo.txt","w")
    fwrite.write(str(ssn))

main()
