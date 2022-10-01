N=int(input())
for i in range(N):
    x=input().split(" ")
    a,b,c=x
    a=float(a)
    b=float(b)
    c=float(c)
    r=(a*2+b*3+c*5)/(2+3+5)
    print(f'{r:.1f}')
