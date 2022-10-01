a = int(input())
for m in range(1,a+1):
    i=int(input())
    if(i%2==0 and i<0):
        print("EVEN NEGATIVE")
    if (i % 2 == 0 and i > 0):
        print("EVEN POSITIVE")
    if (i % 2 != 0 and i < 0):
        print("ODD NEGATIVE")
    if (i % 2 != 0 and i>0):
        print("ODD POSITIVE")
    if (i==0):
        print("NULL")
