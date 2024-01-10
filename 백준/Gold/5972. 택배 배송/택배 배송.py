import heapq
import sys

INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
d = [INF] * N

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s - 1].append((e - 1, c))
    graph[e - 1].append((s - 1, c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    d[start] = 1

    while hq:
        total_cost, now = heapq.heappop(hq)

        for target, cost in graph[now]:
            if d[target] > total_cost + cost:
                d[target] = total_cost + cost
                heapq.heappush(hq, (d[target], target))


dijkstra(0)

print(d[N - 1])
