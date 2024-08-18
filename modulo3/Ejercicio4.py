from bisect import bisect_left

n = int(input())
ids = tuple(map(int, input().split()))
ids_sorted = tuple(sorted(ids))
for _ in range(int(input())):
    couple = tuple(map(int, input().split()))
    couple_sorted = tuple(sorted(couple))
    index_1 = bisect_left(ids_sorted, couple_sorted[0])
    index_2 = bisect_left(ids_sorted, couple_sorted[1])
    print(index_2 - index_1, 'kms')
