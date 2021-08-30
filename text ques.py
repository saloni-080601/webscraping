i=1
while i<=1000:
    j=1
    f=0
    while i>=j:
        if i%j==0:
            f=f+1
        j+=1
    if f==2:
        print(i,"it is prime no")
    i+=1

            
    