n = int(input())
lst = [int(input()) for _ in range(n)]

nums = [0]*11

nums[1], nums[2], nums[3] = 1, 2, 4

for i in range(4, 11):
    nums[i] = nums[i-1] + nums[i-2] + nums[i-3]

for t in lst:
    print(nums[t])