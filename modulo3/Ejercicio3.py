from bisect import bisect_left

cases = int(input())
for _ in range(cases):
    info = tuple(map(int, input().split()))
    nums = tuple(map(int, input().split()))
    p = info[1]
    isPrimi = True
    for i in range(1, p + 1):
        if p % i == 0:
            index = bisect_left(nums, i)
            if index == info[0] or nums[index] != i:
                print('No es PrimiConjunto')
                isPrimi = False
                break
    if isPrimi:
        print('Es PrimiConjunto')
