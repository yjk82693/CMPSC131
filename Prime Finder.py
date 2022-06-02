def PrimeFinder(n):
    mode = input("Select mode: ")
    x = int(n)
    if mode == "Larger":
        k=0
        while k<5:
            a=2
            while a<=n//2:
                if x%a== 0:
                    break
                a+=1
            else:
                print(x, end = ' ')
                k+=1
            x+=1
    else:
        k=0
        while k<5:
            a=2
            while(a<=x//2):
                if(x%a==0):
                    break
                a+=1
            else:
                print(x, end = ' ')
                k+=1
            x-=1
            if(x<2):
                break
