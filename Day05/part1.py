def goodUpdate(list, dict):
    for i in range(len(list)):
        for current in range(0, i):
            if int(list[i]) not in dict:
                continue
            for value in dict[int(list[i])]:
                if value == current:
                    return False
    return True

def main():
    result = 0
    updates = []
    secondPart = False
    dict = {}
    with open("2024/Day05/input.txt", 'r') as file:
        for line in file:
            if line == "\n":
                secondPart = True
                continue
            if secondPart:
                match = line.strip().split(",")
                updates.append(match)
            else:
                match = line.strip().split("|")
                key = int(match[0])
                if key not in dict:
                    dict[key] = []
                dict[key].append(int(match[1]))
    for update in updates:
        if goodUpdate(update, dict):
            result += int(update[int(len(update) // 2)])
    return result

print(main())
