import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic DisjointSet operations."""
    ds = DisjointSet(5)
    
    # Initially, each element should be in its own set
    assert ds.find(0) != ds.find(1)
    
    # After union, they should be in the same set
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)

def test_disjoint_set_multiple_unions():
    """Test multiple union operations."""
    ds = DisjointSet(5)
    
    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(0, 2)
    
    # 0, 1, 2, 3 should now be in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)
    assert ds.find(4) != ds.find(0)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Graph edges: (weight, u, v)
    graph = [
        (1, 0, 1),  # Edge between vertex 0 and 1 with weight 1
        (2, 1, 2),  # Edge between vertex 1 and 2 with weight 2
        (3, 0, 2),  # Edge between vertex 0 and 2 with weight 3
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have two edges with minimum total weight
    assert len(mst) == 2
    assert sum(edge[0] for edge in mst) == 3

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph."""
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (1, 7, 6),
        (2, 8, 6),
        (6, 2, 3),
        (4, 2, 5),
        (2, 3, 5),
        (7, 3, 4),
        (9, 4, 5),
        (10, 4, 6)
    ]
    
    mst = kruskal_mst(graph)
    
    # Total edges in MST should be (vertices - 1)
    assert len(mst) == 8
    
    # Calculate total weight of MST
    mst_weight = sum(edge[0] for edge in mst)
    assert mst_weight == 37

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    graph = []
    
    mst = kruskal_mst(graph)
    
    assert len(mst) == 0

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with a single vertex graph."""
    graph = [(1, 0, 0)]
    
    mst = kruskal_mst(graph)
    
    assert len(mst) == 0  # No MST for a single vertex graph

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph."""
    graph = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Total edges in MST should be (connected_components - 1)
    assert len(mst) == 2