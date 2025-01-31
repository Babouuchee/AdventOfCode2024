def is_safe(seq):
    is_increasing = all(seq[i] < seq[i + 1] and 1 <= seq[i + 1] - seq[i] <= 3 for i in range(len(seq) - 1))
    is_decreasing = all(seq[i] > seq[i + 1] and 1 <= seq[i] - seq[i + 1] <= 3 for i in range(len(seq) - 1))
    return is_increasing or is_decreasing

def can_be_safe_with_removal(seq):
    for i in range(len(seq)):
        if is_safe(seq[:i] + seq[i + 1:]):
            return True
    return False

def main():
    safe_count = 0
    with open("2024/Day02/input.txt", 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels) or can_be_safe_with_removal(levels):
                safe_count += 1
    return safe_count

print(main())
