n=int(input())
h=n//3600
m1=n%3600
m=m1//60
s=m1%60
print(f'{h}:{m}:{s}')