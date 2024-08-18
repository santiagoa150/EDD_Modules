import heapq

dictionary = {'A': [], 'B': [], 'C': [], 'A_': False, 'B_': False, 'C_': False}
A_points, B_points, C_points = 0, 0, 0

while True:
    line = input()
    if line == 'fin del juego':
        print(f"Equipo A: {A_points}")
        print(f"Equipo B: {B_points}")
        print(f"Equipo C: {C_points}")
        break
    elif line == 'menores':
        teams = []
        for team in ['A', 'B', 'C']:
            if len(dictionary[team]) > 0:
                heapq.heappush(teams, dictionary[team][0])
                dictionary[team + "_"] = True
        if len(teams) > 0:
            minus = teams[0]
            if dictionary['A_']:
                if minus == dictionary['A'][0]:
                    A_points += 1
                dictionary['A_'] = False
                heapq.heappop(dictionary['A'])

            if dictionary['B_']:
                if minus == dictionary['B'][0]:
                    B_points += 1
                dictionary['B_'] = False
                heapq.heappop(dictionary['B'])

            if dictionary['C_']:
                if minus == dictionary['C'][0]:
                    C_points += 1
                dictionary['C_'] = False
                heapq.heappop(dictionary['C'])
    else:
        line = line.split()
        heapq.heappush(dictionary[line[0]], int(line[1]))
