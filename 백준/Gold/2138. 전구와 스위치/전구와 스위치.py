import sys
from collections import deque

INF = sys.maxsize

N = int(input())
current = input()
target = input()
dq = deque()
light = [0, 1]

answer = -1
dq.append([-1, int(current[0])])
dq.append(0)

for i in range(N - 1):
    if len(dq) == 0:
        print(-1)
        break

    for _ in range(int(len(dq) / 2)):
        bulbs = dq.popleft()
        cnt = dq.popleft()

        bulbs.append(int(current[i + 1]))

        for l in light:
            if bulbs[0] == -1 or (bulbs[0] + l) % 2 == int(target[i - 1]):
                tmp = [bulbs[1] + l, bulbs[2] + l]
                dq.append(tmp)
                dq.append(cnt + l)

while dq:
    bulbs = dq.popleft()
    cnt = dq.popleft()
    for l in light:
        if (bulbs[0] + l) % 2 == int(target[N - 2]) and (bulbs[1] + l) % 2 == int(target[N - 1]):
            if answer == -1 or answer > cnt + l:
                answer = cnt + l
print(answer)
