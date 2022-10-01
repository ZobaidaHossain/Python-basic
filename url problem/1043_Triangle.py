x,y,z=input().split()
x=float(x)
y=float(y)
z=float(z)
if((x+y)>z and (y+z)>x and (z+x)>y):
    p=x+y+z
    print("Perimetro =",p)
else:
    a=(1/2)*(x+y)*z
    print("Area =",a)