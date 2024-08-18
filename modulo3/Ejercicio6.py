cases = int(input())
for _ in range(cases):
    nums = tuple(map(int, input().split(', ')))
    sorted_nums = tuple(sorted(nums))
    n = 0
    current_sum = 0
    all_nums = sum(sorted_nums)
    length = len(sorted_nums) - 1
    response = 0
    while n < length:
        current_sum += sorted_nums[n]

        current_estimate = abs((all_nums - current_sum) - current_sum)
        next_estimate = abs((all_nums - current_sum - sorted_nums[n + 1]) - current_sum - sorted_nums[n + 1])
        if next_estimate > current_estimate:
            response = current_estimate
            break
        else:
            response = next_estimate
        n += 1
    print(response)
