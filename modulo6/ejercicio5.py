import heapq

max_song = int(input())
tones = []
for _ in range(int(input())):
    line = input().split()
    heapq.heappush(tones, (int(line[1]), int(line[2])))

while len(tones) > 0:
    N_tone = heapq.heappop(tones)
    print(N_tone[0])
    next = N_tone[0] + N_tone[1]
    if next <= max_song:
        heapq.heappush(tones, (next, N_tone[1]))
