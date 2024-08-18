words = {}
while True:
    word = input()
    if word == '#':
        break
    words[word] = True

results = []

for word_to_build in words:
    for i in range(1, len(word_to_build)):
        initial = word_to_build[:i]
        final = word_to_build[i:]
        if initial in words and final in words:
            results.append(f'{word_to_build} = {initial} + {final}')

for r in sorted(results):
    print(r)
