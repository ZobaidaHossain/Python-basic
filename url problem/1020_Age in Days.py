n=int(input())
y=n//365
m1=n%365
m=m1//30
s=m1%30
print(f'{y} ano(s)')
print(f'{m} mes(es)')
print(f'{s} dia(s)')