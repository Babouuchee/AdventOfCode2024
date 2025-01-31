import re

def main():
    result = 0
    pattern = re.compile(r"mul\((\d+),(\d+)\)")

    with open("2024/Day03/example.txt", 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                result += int(match[0]) * int(match[1])
    return result

print(main())
