
m=int(input())
ex=[100,50,20,10,5,2,1]
print(m)
for i in ex:
        v=m//i
        m=m%i
        print(v,f'nota(s) de R$ {i},00')


