v=0
sum=0
a=int(input())
b=int(input())
for i in range(b+1,a):
    if(i%2!=0):
        sum=sum+i

print(sum)