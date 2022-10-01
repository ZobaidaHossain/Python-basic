c=input().split(" ")
a,v=c
a=int(a)
v=int(v)
if(a==1):
    res=v*4.00
    print(f'Total: R$ {res:.2f}')
elif(a==2):
    res=v*4.50
    print(f'Total: R$ {res:.2f}')
elif(a==3):
    res=v*5.00
    print(f'Total: R$ {res:.2f}')
elif(a==4):
    res=v*2.00
    print(f'Total: R$ {res:.2f}')
elif(a==5):
    res=v*1.50
    print(f'Total: R$ {res:.2f}')
