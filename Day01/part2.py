def main():
    result = 0
    list = []
    dict = {}
    with open("2024/Day01/input2.txt", 'r') as file:
        for line in file:
            parts = line.split()
            list.append(int(parts[0]))
            secondNb = int(parts[1])
            if secondNb not in dict:
                dict[secondNb] = 0
            dict[secondNb] += 1
    print(dict)
    for item in list:
        if item not in dict:
            continue
        result += item * dict[item]
    return result

list = main()
print(list)
