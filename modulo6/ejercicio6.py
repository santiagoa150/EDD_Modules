import heapq

for _ in range(int(input())):
    line = list(map(int, input().split()))
    nums = [n + 1 for n in range(line[0])]
    heapq.heapify(nums)

    while len(nums) > 1:
        length = len(nums)
        to_delete = length // 2
        for i in range(length):
            nums[i] = (nums[i] * line[1]) % line[2]
        heapq.heapify(nums)
        for i in range(to_delete):
            heapq.heappop(nums)
    print(nums[0])
