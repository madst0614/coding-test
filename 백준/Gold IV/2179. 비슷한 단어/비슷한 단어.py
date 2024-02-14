N = int(input())

list = []
for _ in range(N):
    list.append(input())

S, T = 0, 0
max_voc_list = []
for i in range(N):
    for j in range(i + 1, N):
        idx = 0
        voc_list = []

        while idx < len(list[i]) and idx < len(list[j]):
            if list[i][idx] != list[j][idx]:
                break

            voc_list.append(list[i][idx])
            idx += 1

        if len(voc_list) > len(max_voc_list):
            max_voc_list = voc_list
            S, T = i, j

print(list[S])
print(list[T])