N = int(input())
num_list = [0] + [int(input()) for _ in range(N)]

visit = [False for _ in range(N + 1)]

answer_list = []


def dfs(n):
    if visit_cnt[n] >= 2:
        return

    visit[n] = True
    visit_cnt[n] += 1

    dfs(num_list[n])


for i in range(1, N + 1):

    if not visit[i]:
        visit_cnt = [0 for _ in range(N + 1)]
        dfs(i)

        for j in range(1, N + 1):
            if visit_cnt[j] == 2:
                answer_list.append(j)

answer_set = set(sorted(answer_list))

answer = '\n'.join(str(element) for element in answer_set)

print(len(answer_set))
print(answer)
