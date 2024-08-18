n, number = tuple(map(int, input().split()))
options = set()
for _ in range(n):
    options.add(int(input()))

options2 = options.copy()

results = []

for num1 in options:
    for num2 in options2:
        if num1 != num2 and num1 + num2 < number:
            rest = number - num1 - num2
            if rest in options and rest != num1 and rest != num2:
                new = sorted([rest, num1, num2])
                if new not in results:
                    results.append(new)
    options2.remove(num1)

if len(results) > 0:
    for r in sorted(results):
        print(' '.join(map(str, r)))
else:
    print('No hay trillizas')