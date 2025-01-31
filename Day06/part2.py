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

def isInfinite(map, pos, moves):
    pathing = True
    base_pos = pos
    visitedPos = set()
    while pathing:
        pos = moves[pos.h](map, pos)
        if pos not in visitedPos:
            visitedPos.add(pos)
        else:
            return True
        if pos == base_pos:
            return True
        if pos.h == 's':
            return False
    return False

def checkLoop(map, pos: Position, moves):
    block_pos = [1, 2]
    if pos.h == 'u' and (pos.y - 1) > 0:
        block_pos = [pos.y - 1, pos.x]
    elif pos.h == 'd' and (pos.y + 1) < len(map):
        block_pos = [pos.y + 1, pos.x]
    elif pos.h == 'l' and (pos.x - 1) > 0:
        block_pos = [pos.y, pos.x - 1]
    elif pos.h == 'r' and (pos.x + 1) < len(map[0]):
        block_pos = [pos.y, pos.x + 1]
    original_char = map[block_pos[0]][block_pos[1]]
    map[block_pos[0]][block_pos[1]] = '#'
    isLoop = isInfinite(map, pos, moves)
    map[block_pos[0]][block_pos[1]] = original_char
    return isLoop

def guardPath(map, pos):
    result = 0
    pathing = True
    moves = {
        'u': move_up,
        'd': move_down,
        'l': move_left,
        'r': move_right
    }
    while pathing:
        # print(pos)
        if (checkLoop(map, pos, moves)):
            result += 1
        pos = moves[pos.h](map, pos)
        if pos.h == 's':
            pathing = False
    return result

def main():
    map = []
    with open("2024/Day06/input.txt", 'r') as file:
        for line in file:
            map.append(list(line.strip()))
    pos = findGuard(map)
    return guardPath(map, pos)

print(main())
