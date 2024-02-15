N = int(input())

list = []

dp = [1 for _ in range(N)]
cont_max = 0
for i in range(N):
    list.append(int(input()))

    for j in range(i):
        if list[j] < list[i]:
            dp[i] = max(dp[i], dp[j]+1)

    cont_max = max(dp[i], cont_max)

print(N - cont_max)