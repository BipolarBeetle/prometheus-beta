import pytest
from src.unique_grid_paths import find_shortest_path

def test_simple_grid_path():
    """Test a simple grid with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5

def test_blocked_start():
    """Test when start cell is blocked"""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) is None

def test_blocked_end():
    """Test when end cell is blocked"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) is None

def test_grid_with_blocked_path():
    """Test a grid where direct path is blocked"""
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5

def test_single_cell_grid():
    """Test a single-cell grid"""
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_empty_grid():
    """Test error handling for empty grid"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_non_square_grid():
    """Test error handling for non-square grid"""
    with pytest.raises(ValueError):
        find_shortest_path([
            [0, 0, 0],
            [0, 0]
        ])

def test_complex_grid():
    """Test a more complex grid with multiple blocked paths"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    assert find_shortest_path(grid) == 7

def test_no_possible_path():
    """Test a grid with no possible path"""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) is None