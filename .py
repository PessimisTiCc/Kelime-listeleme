OneOnethousand=list(range(300,400))     
for i in OneOnethousand:
    n=i%10
    if n==1:
        k=i
        print("")        
        for u in list(range(10)):
            k=k+u
            print('""',',','#',k)
            k=k-u
        print("")
        print("**********************************************")
    print('""',',','#',i)
