def max_knapsack(capacity, weights, values):
    if capacity < 0:
        return -float('inf')
    if len(weights) == 0:
        return 0

    with_first = values[0] + max_knapsack(capacity - weights[0], weights[1:], values[1:])
    without_first = max_knapsack(capacity, weights[1:], values[1:])
    return max(with_first, without_first)
