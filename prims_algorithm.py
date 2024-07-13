import heapq

def prim(graph, start):
    mst=[]
    visited=set([start])
    edges=[(cost,start,to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    while edges :
        cost, frm, to =  heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm,to, cost))
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges,(cost2, to, to_next))
    return mst

def parse_input():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node: ")
        graph[node] = {}
        num_neighbors = int(input("Enter the number of neighbors for node {}: ".format(node)))
        for _ in range(num_neighbors):
            neighbor, weight = input("Enter neighbor and weight (separated by space) for node {}: ".format(node)).split()
            graph[node][neighbor] = int(weight)
    return graph

def main():
    graph = parse_input()
    start_node = input("Enter the start node: ")
    print(prim(graph, start_node))

if __name__ == "__main__":
    main()




"""
Output:

Enter the number of nodes: 4
Enter node: a
Enter the number of neighbors for node a: 2
Enter neighbor and weight (separated by space) for node a: b 2
Enter neighbor and weight (separated by space) for node a: c 3
Enter node: b
Enter the number of neighbors for node b: 3
Enter neighbor and weight (separated by space) for node b: a 2
Enter neighbor and weight (separated by space) for node b: c 1
Enter neighbor and weight (separated by space) for node b: d 1
Enter node: c
Enter the number of neighbors for node c: 3
Enter neighbor and weight (separated by space) for node c: a 3
Enter neighbor and weight (separated by space) for node c: b 1
Enter neighbor and weight (separated by space) for node c: d 4
Enter node: d
Enter the number of neighbors for node d: 2
Enter neighbor and weight (separated by space) for node d: b 1
Enter neighbor and weight (separated by space) for node d: c 4
Enter the start node: a
[('a', 'b', 2), ('b', 'c', 1), ('b', 'd', 1)]
"""
