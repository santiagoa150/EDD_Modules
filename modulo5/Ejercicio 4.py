from bisect import bisect_left

nums = []
aux = []
while True:
    num = int(input())
    valid = True
    if num == 0:
        break

    current_index = bisect_left(nums, num)
    last_index = bisect_left(nums, num + 1)

    nums_length = len(nums)

    if current_index != nums_length and nums[current_index] == num:
        del nums[current_index]
        aux.remove(num)
        valid = False
    elif last_index != nums_length and nums[last_index] == num + 1:
        del nums[last_index]
        aux.remove(num + 1)
        valid = False
    elif current_index != 0 and nums[current_index - 1] == num - 1:
        del nums[current_index - 1]
        aux.remove(num - 1)
        valid = False

    if valid:
        nums.insert(current_index, num)
        aux.append(num)

if len(nums) == 0:
    print(0)
else:
    print(*aux)
