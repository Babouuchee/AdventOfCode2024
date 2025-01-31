from collections import defaultdict, deque

def topological_sort(update, rules):
    """Reorder pages in an update using topological sort based on rules."""
    # Build a graph for the pages in the update
    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}
    
    for a, b in rules:
        if a in update and b in update:
            graph[a].append(b)
            in_degree[b] += 1

    # Perform topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def main():
    # Initialize
    result_incorrect = 0
    incorrect_updates = []
    rules = set()
    updates = []
    second_part = False

    # Read and parse input
    with open("2024/Day05/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                second_part = True
                continue
            if second_part:
                updates.append(list(map(int, line.split(","))))
            else:
                a, b = map(int, line.split("|"))
                rules.add((a, b))

    # Process updates
    for update in updates:
        if not is_valid_update(update, rules):
            # Reorder the incorrectly ordered update
            reordered_update = topological_sort(update, rules)
            incorrect_updates.append(reordered_update)
            result_incorrect += reordered_update[len(reordered_update) // 2]

    print("Reordered Incorrect Updates:", incorrect_updates)
    print("Result (Sum of middle pages of reordered updates):", result_incorrect)

def is_valid_update(update, rules):
    """Check if an update respects the ordering rules."""
    page_indices = {page: i for i, page in enumerate(update)}  # Map page to its index in the update
    for a, b in rules:
        if a in page_indices and b in page_indices:
            if page_indices[a] > page_indices[b]:  # Rule violated
                return False
    return True

if __name__ == "__main__":
    main()
