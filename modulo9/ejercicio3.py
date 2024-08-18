import math

to_win = None
for i in range(5):
    nums = [int(input()) for _ in range(int(input()))]
    new_exercise = set(nums)
    if i == 0:
        to_win = set(nums)
    else:
        to_win = to_win & new_exercise

cant = len(to_win)
if cant > 0:
    print(math.floor(1000000 / cant))
else:
    print('Nadie gana')