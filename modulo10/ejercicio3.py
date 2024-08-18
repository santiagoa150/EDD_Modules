M = int(input())
tickets = {}
generated = set()
results = []
while True:
    line = input()
    if line == 'end':
        break
    action, value = line.split()
    if action == 'sms':
        try:
            tickets[value] += 1
        except:
            tickets[value] = 1

        if value in generated:
            results.append(f'{value} {M // (len(generated) * tickets[value])}')
    else:
        generated.add(value)

if len(results) > 0:
    for i in results:
        print(i)
else:
    print(0)
