dr = [1, 0, 1, 1]
dc = [0, 1, 1, -1]
answer = ""


def dfs(i, r, c):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
        bingo[r][c].append(i)
        return True

    if tic[nr][nc] == tic[r][c]:

        if dfs(i, nr, nc):
            bingo[r][c].append(i)
            return True
        else:
            return False

    else:
        return False


while True:
    str = input()

    if str == "end":
        break
    if answer != "":
        answer += "\n"

    tic = [[e for e in str[3 * i: 3 * (i + 1)]] for i in range(3)]
    bingo = [[[] for _ in range(3)] for _ in range(3)]

    bingo_cnt = 0
    x = 0
    o = 0

    valid = True

    for r in range(3):
        for c in range(3):
            if tic[r][c] == '.':
                continue

            if tic[r][c] == 'X':
                x += 1
            if tic[r][c] == 'O':
                o += 1

            if r == 0:
                if c == 0 and dfs(2, r, c):
                    bingo_cnt += 1

                if c == 2 and dfs(3, r, c):
                    bingo_cnt += 1

                if dfs(0, r, c):
                    bingo_cnt += 1

            if c == 0 and dfs(1, r, c):
                bingo_cnt += 1

    if bingo_cnt == 0:
        if x + o < 9:
            valid = False
    elif bingo_cnt == 1:
        for r in range(3):
            for c in range(3):
                if len(bingo[r][c]) == 1:
                    if tic[r][c] == 'O' and x > o:
                        valid = False
                    
                    if tic[r][c] == 'X' and x == o:
                        valid = False
    elif bingo_cnt == 2:
        x_cnt = 0
        for r in range(3):
            for c in range(3):
                if len(bingo[r][c]) > 0 and tic[r][c] == 'O':
                    valid = False
                else:
                    if len(bingo[r][c]) > x_cnt:
                        x_cnt = len(bingo[r][c])
        if x_cnt < 2:
            valid = False

    if abs(x - o) > 1 or o > 4 or o > x:
        valid = False

    if valid:
        answer += "valid"
    else:
        answer += "invalid"

print(answer)
