v=0
sum=0
for i in range(1,7):
    a=float(input())
    if(a>0):
        v=v+1
        sum=sum+a
avg=sum/v
print("%d valores positivos"%v)
print(f'{avg:.1f}')