from collections import deque
N = int(input())
M = int(input())

path = [list(map(int, input().split())) for _ in range(N)]
route = list(map(lambda x: int(x)-1, input().split()))
visited = [False for _ in range(N)]

dq = deque()
dq.append(route[0])

while dq:
    n = dq.pop()

    if visited[n]:
        continue

    visited[n] = True

    for i in range(N):
        if path[n][i] == 1 and not visited[i]:
            dq.append(i)

answer = True

for n in route:
    if not visited[n]:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")