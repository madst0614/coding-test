import sys
import bisect

N = int(input())
sol = list(map(int, input().split()))

a = sys.maxsize
b = 0

for num in sol:
    i = bisect.bisect_left(sol, -num)

    if 0 <= i < len(sol):
        if num != sol[i] and abs(num + sol[i]) < abs(a + b):
            a = num
            b = sol[i]
    if 0 <= i - 1 < len(sol):
        if num != sol[i-1] and abs(num + sol[i - 1]) < abs(a + b):
            a = num
            b = sol[i - 1]

if a > b:
    print(b, a)
else:
    print(a, b)
