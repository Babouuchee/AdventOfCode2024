def checkHorizontal(a, b, list):
    result = 0
    xmas = "XMAS"
    count = 0
    for i in range(4):
        if (b + i >= len(list[a])):
            break
        if xmas[i] == list[a][b + i]:
            count += 1
    if count == 4:
        result += 1
    count = 0
    for i in range(4):
        if (b - i < 0):
            break
        if xmas[i] == list[a][b - i]:
            count += 1
    if count == 4:
        result += 1
    return result

def checkVertical(a, b, list):
    result = 0
    xmas = "XMAS"
    count = 0
    for i in range(4):
        if (a + i >= len(list)):
            break
        if xmas[i] == list[a + i][b]:
            count += 1
    if count == 4:
        result += 1
    count = 0
    for i in range(4):
        if (a - i < 0):
            break
        if xmas[i] == list[a - i][b]:
            count += 1
    if count == 4:
        result += 1
    return result

def checkDiagonal(a, b, list):
    result = 0
    xmas = "XMAS"
    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            count = 0
            for i in range(4):
                if (a + (x * i) < 0) or (b + (y * i) < 0) or (a + (x * i) >= len(list)) or (b + (y * i) >= len(list[a])):
                    break
                if xmas[i] == list[a + (x * i)][b + (y * i)]:
                    count += 1
            if count == 4:
                result += 1
    return result

def main():
    result = 0
    list = []
    with open("2024/Day04/input.txt", 'r') as file:
        for line in file:
            list.append(line.strip())
    for i in range(len(list)):
        for j in range(len(list[i])):
            result += checkHorizontal(i, j, list)
            result += checkVertical(i, j, list)
            result += checkDiagonal(i, j, list)
    return result

print(main())
# 2549
