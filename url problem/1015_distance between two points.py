import math
x=input().split(" ")
x1,y1=x
x1=float(x1)
y1=float(y1)
y=input().split(" ")
x2,y2=y
x2=float(x2)
y2=float(y2)
r=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
res=math.sqrt(r)
print(f'{res:.4f}')