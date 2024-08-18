for _ in range(int(input())):
    info = tuple(map(int, input().split()))
    nums = [n for n in range(1, info[0] + 1)]
    length = info[0]
    k = info[1]
    current = 0
    while length > 1:
        current = current + (k - 1 % length)
        deleted = nums[current]
        del nums[current]
        nums = nums[current:] + nums[:current]
        length -= 1
        k = deleted % length
        current = 0
        if k == 0:
            k = 1
    print(nums[0])
