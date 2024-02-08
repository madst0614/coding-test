N = int(input())
list = list(map(int, input().split()))

s = set()

answer = 0
start = 0
end = 0
s.add(list[start])

while start <= end:
    if end >= N:
        break

    while start < end and list[end] in s:
        s.remove(list[start])
        start += 1
        answer += end-start+1


    s.add(list[end])
    end += 1


if start < end:
    while start <= end:
        start += 1
        answer += end-start+1


print(answer)