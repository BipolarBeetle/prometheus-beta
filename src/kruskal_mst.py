class DisjointSet:
    """
    A data structure to support Kruskal's algorithm using Union-Find.
    
    Implements path compression and union by rank for efficient operations.
    """
    def __init__(self, vertices):
        """
        Initialize disjoint set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            # Path compression: make every node point directly to the root
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was performed, False if already in same set
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)

        # If roots are same, they're already in the same set
        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are same, arbitrarily choose one and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's algorithm.
    
    :param graph: A list of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    
    Time Complexity: O(E log E), where E is the number of edges
    Space Complexity: O(V), where V is the number of vertices
    """
    # Input validation
    if not graph:
        return []

    # Sort edges by weight in ascending order
    sorted_edges = sorted(graph)

    # Find the maximum vertex to determine the number of vertices
    max_vertex = max(max(u, v) for _, u, v in graph)
    vertices = max_vertex + 1

    # Initialize disjoint set
    ds = DisjointSet(vertices)

    # List to store MST edges
    mst = []

    # Iterate through sorted edges
    for weight, u, v in sorted_edges:
        # If including this edge doesn't form a cycle, add it to MST
        if ds.union(u, v):
            mst.append((weight, u, v))

    return mst