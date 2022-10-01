m=float(input())
ex=[100,50,20,10,5,2]
c=[1,0.50,0.25,0.10,0.05,0.01]
print("NOTAS:")
for i in ex:
        print(f'{int(a/i)} nota(s) de R$ {i}.00')
        cc=float(f'{m%i:.2f}')
print("MOEDAS:")
for i in c:
        print(f'{int(a//i)} moeda(s) de R$ {i:.2f}')
        a=float(f'{a%i:.2f}')

