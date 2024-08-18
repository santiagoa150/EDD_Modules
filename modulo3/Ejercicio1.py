from bisect import bisect_left

n = int(input())
nums = tuple(map(int, input().split()))
to_search = int(input())
to_search_nums = tuple(map(int, input().split()))

res = 0

for searching in to_search_nums:
    index = bisect_left(nums, searching)
    if index != n and nums[index] == searching:
        res += index + 1

print(res)
