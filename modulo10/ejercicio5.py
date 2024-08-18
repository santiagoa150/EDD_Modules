votes = {}
voted = {}
while True:
    line = input()
    if line == '0 0':
        break
    user, vote = line.split()
    try:
        cant_vote = voted[user]
    except:
        cant_vote = False

    if cant_vote:
        if not cant_vote[1]:
            votes[cant_vote[0]] -= 1
            voted[user] = (cant_vote[0], True)
    else:
        try:
            votes[vote] += 1
        except:
            votes[vote] = 1
        voted[user] = (vote, False)

votes_mapped = [(valor, int(clave)) for clave, valor in votes.items()]
for i in sorted(votes_mapped, reverse=True):
    if i[0] == 0:
        break
    print(f'{i[1]} {i[0]}')
