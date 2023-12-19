import heapq


N = int(input())
li = []
ans = 0
cnt = N
for _ in range(N):
    for _ in list(map(int, input().split(' '))):
        heapq.heappush(li, _)

    if len(li) >= 2*N:
        for _ in range(N):
            heapq.heappop(li)


print(heapq.heappop(li))