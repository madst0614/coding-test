dr = [0, 1]
dc = [1, 0]

N = int(input())

li = list(map(int, input().split(' ')))

answer = [0 for _ in range(N)]

for i in range(len(li)):
    cnt = li[i]
    idx = 0
    while True:
        if 0 < answer[idx] < i+1:
            idx+=1
            continue

        if cnt == 0:
            answer[idx] = i + 1
            break

        if answer[idx] == 0:
            cnt -= 1

        idx += 1

print(' '.join(str(_) for _ in answer))

