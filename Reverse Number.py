def reverse(n):
    r=0
    count = len(str(n))-1
    if n == 0:
        return r
    else:
        r+= (n%10)*(10**(count))
        count-=1
        return r + reverse(n//10)
    
