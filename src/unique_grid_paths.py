from typing import List, Optional

def find_shortest_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right cell with movement constraints.
    
    Movement constraints:
    - Can move right or down
    - Can only move to an empty cell (0)
    - If right is blocked, must move down
    
    Args:
        grid (List[List[int]]): A 2D grid of 0s and 1s
    
    Returns:
        Optional[int]: Length of the shortest path, or None if no path exists
    
    Raises:
        ValueError: If grid is empty or not square
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    n = len(grid)
    
    # Ensure grid is square
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be square")
    
    # Check start and end points are valid
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return None
    
    # Initialize DP table
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 1
    
    # First row
    for j in range(1, n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1] + 1
        else:
            break
    
    # First column
    for i in range(1, n):
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0] + 1
        else:
            break
    
    # Fill DP table
    for i in range(1, n):
        for j in range(1, n):
            # Skip blocked cells
            if grid[i][j] == 1:
                continue
            
            # Determine possible movements
            if grid[i][j-1] == 0:  # Can move right
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            
            # Always prefer moving down when blocked
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
    
    # Return path length if a path exists
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else None