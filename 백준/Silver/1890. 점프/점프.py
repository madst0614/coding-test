dr = [0, 1]
dc = [1, 0]

N = int(input())

maps = []

for i in range(N):
    maps.append(list(map(int, input().split(' '))))
dp = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
def dfs(r, c):
    if visited[r][c]:
        return dp[r][c]

    if r == N - 1 and c == N - 1:
        return 1

    visited[r][c] = True
    for i in range(2):
        nr = r + maps[r][c]*dr[i]
        nc = c + maps[r][c]*dc[i]

        if valid(nr, nc):
           dp[r][c] += dfs(nr, nc)

    return dp[r][c]


def valid(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


print(dfs(0, 0))
