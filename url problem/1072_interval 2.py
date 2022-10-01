x=int(input())
n=0
m=0
for i in range(x):
    a=int(input())
    if(10<=a<=20):
        n=n+1

    else:
        m=m+1
print("%d in"%n)
print("%d out"%m)