from collections import deque

s = input()
e = input()

stack = deque()

for c in s:
    stack.append(c)

    if c == e[len(e) - 1]:
        tmp = deque()
        cnt = len(e) - 1
        while True:
            if cnt < 0:
                tmp = None
                break

            if len(stack) == 0:
                break

            tmp_c = stack.pop()
            tmp.append(tmp_c)

            if tmp_c != e[cnt]:
                break

            cnt -= 1

        while tmp:
            stack.append(tmp.pop())

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
