import heapq
import sys

INF = sys.maxsize
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

cnt = 0


def dijk(cost):
    cost[0][0] = maps[0][0]

    heap = [[cost[0][0], 0, 0]]

    while heap:
        node = heapq.heappop(heap)

        r = node[1]
        c = node[2]

        if visited[r][c]:
            continue

        visited[r][c] = True
        cost[r][c] = node[0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                heapq.heappush(heap, [cost[r][c] + maps[nr][nc], nr, nc])

    return cost[N - 1][N - 1]


while True:
    cnt += 1
    N = int(input())

    if N == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    cost = [[INF for _ in range(N)] for _ in range(N)]
    print(f"Problem {cnt}: {dijk(cost)}")
