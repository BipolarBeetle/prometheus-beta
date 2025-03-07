def solve_knapsack(values, weights, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        values (list): List of values for each item
        weights (list): List of weights for each item
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing:
            - Maximum total value that can be achieved
            - List of selected item indices
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not values or not weights:
        return 0, []
    
    if len(values) != len(weights):
        raise ValueError("Values and weights lists must have the same length")
    
    if any(w < 0 for w in weights):
        raise ValueError("Weights must be non-negative")
    
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    
    n = len(values)
    
    # Create 2D dynamic programming table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item's weight is more than capacity, skip
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Include current item
                )
    
    # Track selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Return max value and selected items (in reverse order)
    return dp[n][capacity], list(reversed(selected_items))