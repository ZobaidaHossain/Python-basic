import math

v = input().split(" ")
a, b, c = v

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c))) / 2

print("%d eh o maior"% resultado)