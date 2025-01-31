# Add the distance between left list item and right list item and returns the result
def main():
    result = 0
    distance = 0
    list1 = []
    list2 = []
    with open("2024/Day01/input.txt", 'r') as file:
        for line in file:
            parts = line.split()
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
    list1.sort()
    list2.sort()
    print(list1)
    for item1, item2 in zip(list1, list2):
        distance = item1 - item2
        if distance < 0:
            distance = -distance
        result += distance
    return result

list = main()
print(list)
