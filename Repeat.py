def repeat(n):
    mx = 1
    count = 1
    chm = n[0]
    for i in range(len(n)):
        if n[i-1] == n[i]:
            count += 1
        else:
            if count > mx:
                mx = count
                chm = n[i-1]
            count = 1
    return "The longest sequence is",chm,"repeated",mx,"times." 
        
