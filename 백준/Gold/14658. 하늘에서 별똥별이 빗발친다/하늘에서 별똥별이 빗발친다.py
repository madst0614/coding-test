N, M, L, K = map(int, input().split())

stars = []
answer = 0

for _ in range(K):
    stars.append(list(map(int, input().split())))

for i in range(K):
    for j in range(i, K):
        cnt = 0

        sx, sy = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

        for k in range(K):
            if (sx <= stars[k][0] <= sx + L
                    and sy <= stars[k][1] <= sy + L):
                cnt += 1

        if cnt > answer:
            answer = cnt

print(K - answer)
