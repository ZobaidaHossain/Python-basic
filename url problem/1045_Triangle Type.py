x,y,z=sorted(list(map(float,input().split())),reverse=True)
if(x>=(y+z)):
    print("NAO FORMA TRIANGULO")
elif((x*x)==((y*y)+(z*z))):
    print("TRIANGULO RETANGULO")
elif((x*x)>((y*y)+(z*z))):
    print("TRIANGULO OBTUSANGULO")
elif((x*x)<((y*y)+(z*z))):
    print("TRIANGULO ACUTANGULO")
if(x==y==z):
    print("TRIANGULO EQUILATERO")
if((x==y and x!=z) or (y==z and x!=y) or (x==z and y!=x)):
    print("TRIANGULO ISOSCELES")