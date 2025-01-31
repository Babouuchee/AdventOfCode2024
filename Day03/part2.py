import re

def main():
    result = 0
    mulPattern = re.compile("do\(\)|don't\(\)|mul\(\d+,\d+\)")
    enabled = True
    with open("2024/Day03/input1.txt", 'r') as file:
        for line in file:
            matches = mulPattern.finditer(line)
            for match in matches:
                match_text = match.group()
                if match_text == "do()":
                    enabled = True
                elif match_text == "don't()":
                    enabled = False
                elif enabled:
                    numbers = re.findall(r'\d+', match_text)
                    result += int(numbers[0]) * int(numbers[1])
    return result

print(main())
