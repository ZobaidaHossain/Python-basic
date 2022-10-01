h=0
p=0
for i in range(100):
    x=int(input())
    if(x>h):
        h=x
        p=i
print(h)
print(p+1)