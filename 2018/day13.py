from operator import attrgetter

day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

directions = [up, right, down, left]
direction_dict = {'^': up, 'v': down, '<': left, '>': right}
direction_dict_reverse = {up: '^', down: 'v', left: '<', right: '>'}


class Cart():
    def __init__(self, posX, posY, direction):
        self.posX = posX
        self.posY = posY
        self.vecX = direction[0]
        self.vecY = direction[1]
        self._direction = direction
        self.turn = 0

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if self._direction != value:
            self._change_direction(value)
        self._direction = value

    def _change_direction(self, direction):
        self.vecX = direction[0]
        self.vecY = direction[1]

    def turn_left(self):
        self.direction = directions[(directions.index(self.direction) - 1) % 4]

    def turn_right(self):
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def intersection(self):
        if self.turn == 0:
            self.turn_left()
        elif self.turn == 1:
            pass
        elif self.turn == 2:
            self.turn_right()

        self.turn = (self.turn + 1) % 3

    def curve(self, char):
        if self.direction in [up, down]:
            if char == '/':
                self.turn_right()
            else:
                self.turn_left()
        elif self.direction in [right, left]:
            if char == '/':
                self.turn_left()
            else:
                self.turn_right()

    def move(self):
        self.posX += self.vecX
        self.posY += self.vecY


track = ['' for _ in data]
carts = []

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char in ['^', 'v', '<', '>']:
            carts.append(Cart(x, y, direction_dict[char]))
            if char in ['^', 'v']:
                track[y] += '|'
            else:
                track[y] += '-'
        elif char == '\n':
            break
        else:
            track[y] += char


def sort_carts(carts):
    # return sorted(carts, key=lambda x: x.posY * 1000 + x.posX)
    return sorted(carts, key=attrgetter('posY', 'posX'))


def get_colision(carts):
    for first in carts:
        for second in carts:
            if first is second:
                continue
            if first.posX == second.posX and first.posY == second.posY:
                return [first.posX, first.posY, first, second]
    return None


def print_with_carts(track, carts):
    track = track.copy()
    for cart in sort_carts(carts):
        track[cart.posY] = track[cart.posY][:cart.posX] +\
                           direction_dict_reverse[cart.direction] +\
                           track[cart.posY][cart.posX + 1:]

    for line in track:
        print(line)


tick = 0
while True:
    # print_with_carts(track, carts)
    if len(carts) == 1:
        print("Last cart on tick " + str(tick))
        print("X: " + str(carts[0].posX) + ", Y: " + str(carts[0].posY))
        exit()
    for cart in sort_carts(carts):
        char = track[cart.posY][cart.posX]
        if char in ['/', '\\']:
            cart.curve(char)
        elif char in ['+']:
            cart.intersection()
        cart.move()
        colision = get_colision(carts)
        if colision is not None:
            print("Colision on tick " + str(tick))
            print("X: " + str(colision[0]) + ", Y: " + str(colision[1]))
            carts.remove(colision[2])
            carts.remove(colision[3])

    tick += 1
