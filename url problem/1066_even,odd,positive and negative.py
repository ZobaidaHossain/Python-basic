n=0
p=0
e=0
od=0
for i in range(1,6):
        a=int(input())
        if(a<0):
                n=n+1
        if(a>0):
                p=p+1
        if(a%2==0):
                e=e+1
        if(a%2!=0):
                od=od+1
print("%d valor(es) par(es)"%e)
print("%d valor(es) impar(es)"%od)
print("%d valor(es) positivo(s)"%p)
print("%d valor(es) negativo(s)"%n)
