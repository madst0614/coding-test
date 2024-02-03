from collections import deque

R, C = map(int, input().split())

INF = 10001
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

maps = [input() for _ in range(R)]
jh = [[INF for _ in range(C)] for _ in range(R)]

dq = deque()
answer = INF

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'F':
            dq.append([i, j, 0])

while dq:
    r, c, t = dq.popleft()

    if jh[r][c] > t:
        jh[r][c] = t
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != '#' and jh[nr][nc] > t + 1:
                dq.append([nr, nc, t+1])

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'J':
            dq.append([i, j, 0])
            break

while dq:
    r, c, t = dq.popleft()

    if jh[r][c] > t:
        jh[r][c] = -1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                if answer > t+1:
                    answer = t+1
            elif maps[nr][nc] != '#' and jh[nr][nc] > t + 1:
                dq.append([nr, nc, t+1])

if answer == INF:
    print("IMPOSSIBLE")
else:
    print(answer)
