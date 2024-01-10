H, W = map(int, input().split(" "))
blocks = list(map(int, input().split(" ")))
answer = 0
first_max = 0
max_idx = 0


def left_max(idx):
    left_max = 0
    for i in range(idx):
        if blocks[i] > left_max:
            left_max = blocks[i]

    return left_max


def right_max(idx):
    right_max = 0
    for i in range(idx, W):
        if blocks[i] > right_max:
            right_max = blocks[i]

    return right_max


for i in range(W):
    total_min = min(left_max(i), right_max(i))

    if total_min > blocks[i]:
        answer += total_min - blocks[i]

print(answer)
