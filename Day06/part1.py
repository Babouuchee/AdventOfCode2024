from collections import namedtuple

Position = namedtuple('Position', ['y', 'x', 'h'])

def findGuard(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == '^':
                return Position(y, x, 'u')
    return None

def move_up(map, pos):
    if pos.y - 1 < 0:
        return Position(pos.y, pos.x, 's')
    if map[pos.y - 1][pos.x] == '#':
        return Position(pos.y, pos.x + 1, 'r')
    return Position(pos.y - 1, pos.x, 'u')

def move_down(map, pos):
    if pos.y + 1 >= len(map):
        return Position(pos.y, pos.x, 's')
    if map[pos.y + 1][pos.x] == '#':
        return Position(pos.y, pos.x - 1, 'l')
    return Position(pos.y + 1, pos.x, 'd')

def move_left(map, pos):
    if pos.x - 1 < 0:
        return Position(pos.y, pos.x, 's')
    if map[pos.y][pos.x - 1] == '#':
        return Position(pos.y - 1, pos.x, 'u')
    return Position(pos.y, pos.x - 1, 'l')

def move_right(map, pos):
    if pos.x + 1 >= len(map[0]):
        return Position(pos.y, pos.x, 's')
    if map[pos.y][pos.x + 1] == '#':
        return Position(pos.y + 1, pos.x, 'd')
    return Position(pos.y, pos.x + 1, 'r')

def guardPath(map, pos: Position):
    result = 1
    pathing = True
    moves = {
        'u': move_up,
        'd': move_down,
        'l': move_left,
        'r': move_right
    }
    visitedPositions = set()
    while pathing:
        print(pos)
        visitedPositions.add((pos.y, pos.x))
        pos = moves[pos.h](map, pos)
        if pos.h == 's':
            pathing = False
        if (pos.y, pos.x) not in visitedPositions:
            result += 1
    return result

def main():
    map = []
    with open("2024/Day06/example.txt", 'r') as file:
        for line in file:
            map.append(line.strip())
    pos = findGuard(map)
    if pos == None:
        return -1
    return guardPath(map, pos)

print(main())
