N = float(input())

if 0 < N < 1000000:
    print('NOTAS:')
    for i in [100, 50, 20, 10, 5, 2]:
        print('%d nota(s) de R$ %d.00' %((N//i),i))
        N %= i

    print('MOEDAS:')
    for i in [1, 0.5, 0.25, 0.10, 0.05, 0.01]:
        print('%d moeda(s) de R$ %.3f' %((N//i),i))
        N %= i


