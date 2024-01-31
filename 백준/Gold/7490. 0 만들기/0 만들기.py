oper = ['+', '-', ' ']
T = int(input())


def dfs(idx, answer, char_list):
    if idx == N:
        math_exp_list = [char for char in char_list if char != ' ']
        math_exp = ''.join(math_exp_list)

        if eval(math_exp) == 0:
            char_list.append('\n')
            answer.append(''.join(char_list))
            char_list.pop()

        return

    for op in oper:
        char_list.append(op)
        char_list.append(chr(idx + 1 + ord('0')))
        dfs(idx + 1, answer, char_list)
        char_list.pop()
        char_list.pop()


for _ in range(T):
    N = int(input())
    answer = []
    dfs(1, answer, ['1'])
    answer.sort()
    print(''.join(answer))
