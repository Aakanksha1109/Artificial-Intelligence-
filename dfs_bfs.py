def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in sorted(graph[node]):
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)  # Mark start node as visited
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {}
    nodes = input("Enter nodes separated by comma: ").split(',')

    for node in nodes:
        edges = input(f"Enter edges for node {node} (comma-separated): ").split(',')
        graph[node] = sorted(edges)

    start_node = input("Enter the starting node for DFS and BFS: ")

    print("The following is DFS:")
    dfs(graph, start_node, set())
    print()

    print("The following is BFS:")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()







"""
Output:

Enter nodes separated by comma: a,b,c,d,e,f,g
Enter edges for node a (comma-separated): b,c
Enter edges for node b (comma-separated): d,e
Enter edges for node c (comma-separated): f,g
Enter edges for node d (comma-separated): b
Enter edges for node e (comma-separated): b
Enter edges for node f (comma-separated): c
Enter edges for node g (comma-separated): c
Enter the starting node for DFS and BFS: a
The following is DFS:
a b d e c f g 
The following is BFS:
a b c d e f g 
"""
