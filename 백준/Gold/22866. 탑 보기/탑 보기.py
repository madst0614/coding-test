from collections import deque

N = int(input())

height = list(map(int, input().split()))
near = []
answer = []

stack = deque()

for i in range(N):
    temp_near = [0]
    while stack:
        prev = stack.pop()

        if height[prev] > height[i]:
            temp_near.append(prev)
            stack.append(prev)
            break

    if len(stack) > 0:
        temp_near[0] += len(stack)

    stack.append(i)
    near.append(temp_near)

stack.clear()

for i in range(N - 1, -1, -1):
    temp_near = [0]

    while stack:
        prev = stack.pop()
        if height[prev] > height[i]:
            temp_near.append(prev)
            stack.append(prev)
            break

    if len(stack) > 0:
        temp_near[0] += len(stack)

    if near[i][0] > 0 and temp_near[0] > 0:
        if abs(near[i][1] - i) > abs(i - temp_near[1]):
            near[i][1] = temp_near[1]
    elif temp_near[0] > 0:
        near[i].append(temp_near[1])

    stack.append(i)
    near[i][0] += temp_near[0]

for i in range(N):
    if near[i][0] > 0:
        print(near[i][0], near[i][1]+1)
    else:
        print(near[i][0])
