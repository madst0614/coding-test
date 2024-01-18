from collections import deque

N = int(input())

s = deque()

answer = 0
for _ in range(N):
    [i, h] = map(int, input().split())

    if h == 0:
        answer += len(s)
        s.clear()
    else:
        if len(s) == 0:
            s.append(h)
        else:
            if h > s[-1]:
                s.append(h)
            elif h < s[-1]:
                while s:
                    if s[-1] > h:
                        answer += 1
                        s.pop()
                    else:
                        break

                if len(s) == 0 or s[-1] < h:
                    s.append(h)

answer += len(s)
print(answer)
