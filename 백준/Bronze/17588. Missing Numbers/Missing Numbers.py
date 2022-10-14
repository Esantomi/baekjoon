n = int(input())
nums = [int(input()) for _ in range(n)]

if list(range(1, nums[-1]+1)) == sorted(nums):
    print('good job')
else:
    for i in range(1, nums[-1]+1):
        if i not in nums:
            print(i)