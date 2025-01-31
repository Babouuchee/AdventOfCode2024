def checkX(i, j, list):
    count = 0
    char1 = ''
    char2 = ''
    if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(list) or j + 1 >= len(list[i]):
        return 0
    char1 = list[i - 1][j - 1]
    char2 = list[i - 1][j + 1]
    if (char1 == 'M' and list[i + 1][j + 1] == 'S') or (char1 == 'S' and list[i + 1][j + 1] == 'M'):
        count += 1
    if (char2 == 'M' and list[i + 1][j - 1] == 'S') or (char2 == 'S' and list[i + 1][j - 1] == 'M'):
        count += 1
    if count == 2:
        return 1
    return 0

def main():
    result = 0
    list = []
    with open("2024/Day04/input.txt", 'r') as file:
        for line in file:
            list.append(line.strip())
    for i in range(1, len(list) - 1):
        for j in range(1, len(list[i]) - 1):
            if (list[i][j] == 'A'):
                result += checkX(i, j, list)
    return result

print(main())
