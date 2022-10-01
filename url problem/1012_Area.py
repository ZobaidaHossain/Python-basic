a=input().split(" ")
A,B,C=a
A=float(A)
B=float(B)
C=float(C)
triangle=(A*C)*(1/2)
radius=3.14159*C*C
trapezium=C*(A+B)*(1/2)
square=B*B
rectangle=A*B
print(f'TRIANGULO: {triangle:.3f}')
print(f'CIRCULO: {radius:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rectangle:.3f}')