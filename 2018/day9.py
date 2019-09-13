day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

players = int(data[0].split()[0])
last_marble = int(data[0].split()[6])

marbles = [0]
current_player = 0
current_index = 0
current_marble = 1

scores = [0 for _ in range(players)]

while(current_marble < last_marble):
    if current_marble % 23 == 0:
        scores[current_player] += current_marble
        current_index = (current_index - 7) % len(marbles)
        scores[current_player] += marbles.pop(current_index)
    else:
        current_index = (current_index + 2) % len(marbles)
        marbles.insert(current_index, current_marble)

    current_player = (current_player + 1) % players
    current_marble += 1

print(max(scores))

# part 2:

last_marble *= 100

marbles = [0]
current_player = 0
current_index = 0
current_marble = 1

scores = [0 for _ in range(players)]

while(current_marble < last_marble):
    if current_marble % 23 == 0:
        scores[current_player] += current_marble
        current_index = (current_index - 7) % len(marbles)
        scores[current_player] += marbles.pop(current_index)
    else:
        current_index = (current_index + 2) % len(marbles)
        marbles.insert(current_index, current_marble)

    current_player = (current_player + 1) % players
    current_marble += 1

print(max(scores))
