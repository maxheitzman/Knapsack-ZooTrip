# Max Heitzman & Hayden McKinney
# CS 3364 – Dr. Chinta
# Final Project – Part 2: Intergalactic Zoo Trip (0/1 Knapsack)

from typing import List

# Item object to store ID, weight, and biodiversity score
class Item:
    def __init__(self, item_id: int, weight: int, biodiversity_score: int):
        self.item_id = item_id
        self.weight = weight
        self.biodiversity_score = biodiversity_score

# Solves the 0/1 knapsack problem using bottom-up dynamic programming
def solve_knapsack(items: List[Item], capacity: int) -> tuple[int, List[Item]]:
    n = len(items)

    # Create a 2D DP table where dp[i][w] holds the best score using first i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight > w:
                dp[i][w] = dp[i - 1][w]  # item doesn't fit, skip it
            else:
                # Choose between taking or skipping the item
                include = dp[i - 1][w - items[i - 1].weight] + items[i - 1].biodiversity_score
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)

    # Backtrack to find which items were included in the final solution
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        item = items[i - 1]
        if w >= item.weight and dp[i][w] == dp[i - 1][w - item.weight] + item.biodiversity_score:
            selected.append(item)
            w -= item.weight

    return dp[n][capacity], selected

# Outputs the results in a readable format
def print_results(max_score: int, selected: List[Item]):
    print("\n----Part 2: Intergalactic Zoo Trip (0/1 Knapsack)----")
    print("    ----Intergalactic Zoo Trip Equipment Plan----")
    print("\nSelected Items:")
    print(f"{'ID':<6}{'Weight':<10}{'Biodiversity':<15}")
    print("-" * 32)
    for item in reversed(selected):
        print(f"{item.item_id:<6}{item.weight:<10}{item.biodiversity_score:<15}")
    total_weight = sum(item.weight for item in selected)
    print(f"\nTotal Weight Used: W =  {total_weight}")
    print(f"Maximum Biodiversity Score: {max_score}")

# Main function to define items and run the solver
def main():
    items = [
        Item(1, 6, 1600),
        Item(2, 4, 1000),
        Item(3, 5, 1800),
        Item(4, 3, 1200),
        Item(5, 7, 2000)
    ]
    capacity = 18
    max_score, selected_items = solve_knapsack(items, capacity)
    print_results(max_score, selected_items)

if __name__ == "__main__":
    main()
