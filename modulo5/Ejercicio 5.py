M = int(input())
nums = []
nums_length = 0
while True:
    num = int(input())
    if num == 0:
        break
    nums_length += 1
    nums.append(num)

    if nums_length % M == 0:
        nums = sorted(nums)
        if nums_length % 2 == 0:
            half = int(nums_length / 2)
            floor = nums[half - 1]
            ceil = nums[half]
            sum_nums = floor + ceil
            calc = sum_nums / 2
            if calc.is_integer():
                print(int(calc))
            else:
                print(f'{sum_nums}/{2}')
        else:
            print(nums[nums_length // 2])
