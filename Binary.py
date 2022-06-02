def binary(n):
    digit = 0 
    bi = str(n)
    if len(bi) == 0:
        return digit
    else:
        if bi[0] == '1':
            digit+=2**(len(bi)-1)
            return digit+binary(bi[1:])
        elif bi[0] == '0':
            return digit+binary(bi[1:])
        else:
            return "Not available"




