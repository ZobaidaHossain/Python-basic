
x=input().split(" ")
a,b,c=x
a=float(a)
b=float(b)
c=float(c)
s=(b*b)-(4*a*c)
sq=pow(s,.5)
d=2*a
if(s<0 or d==0):
    print("Impossivel calcular")
else:
    r1=(-b+sq)/d
    r2=(-b-sq)/d
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')