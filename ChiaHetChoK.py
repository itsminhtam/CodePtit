A, k, n = input().split()
K = int(k)
N = int(n)
a = int(A)
if N - a <= 0:
    print(-1)
else:
    dem = 0
    loop = N//K + 1
    for i in range(loop):
        if K*i <= N and K*i > a:
            print(K*i-a,end=' ')
            dem += 1
    if dem == 0:
        print(-1)