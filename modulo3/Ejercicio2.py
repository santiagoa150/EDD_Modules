from bisect import bisect

for i in range(int(input())):
    nums = tuple(map(int, input().split()))
    nums = tuple(sorted(nums))
    response = ""
    total = 0
    n = len(nums)
    for j, number in enumerate(nums):
        total += 1
        if j == n-1 or number != nums[j+1]:
            response = response + " " + str(total)
            total = 0
    print(response.lstrip())