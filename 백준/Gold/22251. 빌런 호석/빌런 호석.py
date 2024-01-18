num = [[] for _ in range(10)]
num[0] = [True, True, True, False, True, True, True]
num[1] = [False, False, True, False, False, True, False]
num[2] = [True, False, True, True, True, False, True]
num[3] = [True, False, True, True, False, True, True]
num[4] = [False, True, True, True, False, True, False]
num[5] = [True, True, False, True, False, True, True]
num[6] = [True, True, False, True, True, True, True]
num[7] = [True, False, True, False, False, True, False]
num[8] = [True, True, True, True, True, True, True]
num[9] = [True, True, True, True, False, True, True]

transfer = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i < j:
            cnt = 0
            for k in range(7):
                if num[i][k] != num[j][k]:
                    cnt += 1
            transfer[i][j] = cnt
            transfer[j][i] = cnt

N, K, P, X = map(int, input().split())

answer = 0
for n in range(1, N + 1):

    cnt = 0
    target = X
    tmp = n
    for k in range(K):
        cnt += transfer[target % 10][tmp % 10]

        target //= 10
        tmp //= 10

    if 1 <= cnt <= P:
        answer += 1

print(answer)
