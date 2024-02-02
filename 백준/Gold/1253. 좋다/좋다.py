import bisect
N = int(input())

nums = list(map(int, input().split()))
goods = [False for _ in range(N)]

nums.sort()
answer = 0

for i in range(N):
    left, right = 0, N-1

    while left < right:

        if nums[i] == nums[left] + nums[right]:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                answer += 1
                break
        elif nums[i] < nums[left] + nums[right]:
            right -= 1
        else:
            left += 1

print(answer)