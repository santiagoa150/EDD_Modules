cases = int(input())
for _ in range(cases):
    nums = tuple(map(int, input().split()))
    size = len(nums)
    movements = 0
    for i in range(size - 1):
        for j in range(0, size-i-1):
            if nums[j] > nums[j+1]:
                movements += 1
                nums = nums[:j] + (nums[j+1],) +(nums[j],) + nums[j+2:]

    print(movements)
