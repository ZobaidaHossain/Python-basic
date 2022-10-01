A,B,C,D = map(float,input().split())
r = (A*2+B*3+C*4+D*1)/10
print(f'Media: {r:.1f}')
if r>=7.0:
    print("Aluno aprovado.")
elif r<5.0:
    print("Aluno reprovado.")
elif r>=5.0 and r<7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (r+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')
