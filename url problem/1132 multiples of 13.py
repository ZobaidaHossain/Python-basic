x=int(input())
y=int(input())
sum=0

if(x>y):
    a=y
    b=x
if(x<y):
    a=x
    b=y
for i in range(a,b+1):
    if(i%13!=0):
        sum=sum+i
print(sum)
