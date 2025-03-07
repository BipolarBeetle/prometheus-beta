import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_inputs():
    max_value, selected_items = solve_knapsack([], [], 100)
    assert max_value == 0
    assert selected_items == []

def test_zero_capacity():
    values = [10, 20, 30]
    weights = [5, 10, 15]
    capacity = 0
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 0
    assert selected_items == []

def test_small_capacity():
    values = [10, 20, 30]
    weights = [5, 10, 15]
    capacity = 5
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 10
    assert selected_items == [0]

def test_invalid_inputs():
    with pytest.raises(ValueError, match="Values and weights lists must have the same length"):
        solve_knapsack([1, 2], [1], 10)
    
    with pytest.raises(ValueError, match="Weights must be non-negative"):
        solve_knapsack([1, 2], [1, -2], 10)
    
    with pytest.raises(ValueError, match="Capacity must be non-negative"):
        solve_knapsack([1, 2], [1, 2], -10)

def test_all_items_fit():
    values = [10, 20, 30]
    weights = [5, 10, 15]
    capacity = 50
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 60
    assert set(selected_items) == {0, 1, 2}

def test_single_item():
    values = [100]
    weights = [20]
    capacity = 50
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 100
    assert selected_items == [0]

def test_complex_case():
    values = [50, 100, 150, 200]
    weights = [10, 20, 30, 40]
    capacity = 50
    max_value, selected_items = solve_knapsack(values, weights, capacity)
    assert max_value == 350
    assert set(selected_items) == {0, 1, 3}