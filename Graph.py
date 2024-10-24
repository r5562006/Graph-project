class Graph:
    def __init__(self):
        # Initialize an empty graph with an adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # Print the adjacency list of the graph
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(map(str, self.graph[vertex]))}")

    def bfs(self, start):
        # Perform Breadth-First Search (BFS) from the start vertex
        visited = set()
        queue = [start]
        bfs_order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend([v for v in self.graph.get(vertex, []) if v not in visited])

        return bfs_order

    def dfs(self, start):
        # Perform Depth-First Search (DFS) from the start vertex
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                stack.extend([v for v in self.graph.get(vertex, []) if v not in visited])

        return dfs_order

if __name__ == "__main__":
    # Create an instance of Graph
    g = Graph()
    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Graph adjacency list:")
    g.print_graph()

    print("\nBFS starting from vertex 2:")
    print(g.bfs(2))

    print("\nDFS starting from vertex 2:")
    print(g.dfs(2))