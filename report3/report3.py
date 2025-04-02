def is_safe(graph, node, color, colors_assigned):
    """Checks if assigning a color to a node is safe (no adjacent nodes share the same color)."""
    for neighbor in graph[node]:
        if colors_assigned[neighbor] == color:
            return False
    return True

def graph_coloring_backtrack(graph, k, colors_assigned, node=0):
    """Backtracking function to find a valid coloring assignment."""
    if node == len(graph):  # All nodes are colored
        return True
    
    for color in range(1, k+1):
        if is_safe(graph, node, color, colors_assigned):
            colors_assigned[node] = color
            if graph_coloring_backtrack(graph, k, colors_assigned, node + 1):
                return True
            colors_assigned[node] = 0  # Backtrack
    
    return False

def solve_graph_coloring():
    """Takes user input and determines if a valid graph coloring is possible."""
    # User inputs for N, M, and K
    n, m, k = map(int, input("Enter N (vertices), M (edges), and K (colors): ").split())
    
    # Initialize adjacency list for the graph
    graph = {i: [] for i in range(n)}
    
    # Read edges from user
    print("Enter the edges (u v):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize color assignments
    colors_assigned = [0] * n
    
    # Check if coloring is possible
    if graph_coloring_backtrack(graph, k, colors_assigned):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", colors_assigned)
    else:
        print(f"Coloring Not Possible with {k} Colors")

# Run the program
if __name__ == "__main__":
    solve_graph_coloring()
