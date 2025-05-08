from collections import defaultdict,deque
import random
Array_of_edges_original = [[7,5],[7,6],[5,4],[5,2],[6,4],[6,3],[2,1],[3,1],[1,0]]
# Convert Array of Edges to Adjacency List
def convert_to_list(Array_of_edges_original):
    D = defaultdict(list)
    for u, v in Array_of_edges_original:
        D[u].append(v)
    print("=" * 165)
    print("Reconstructed Adjacency List : \n", D)
    print("=" * 165)
    return D
D1 = convert_to_list(Array_of_edges_original)
# find all indegrees of all nodes in graph
def find_indegree(D):
    indegree = defaultdict(int)
    for u in D:
        if u not in indegree:
            indegree[u] = 0
        for v in D[u]:
            indegree[v] += 1
    print("In-degree of each node:", dict(indegree))
    print("=" * 165)
    return indegree
#find all indegrees of zeros in graph
def pick_random_indegree_node(indegree):
    zero_indegree = [node for node in indegree_data if indegree_data[node] == 0]
    source = random.choice(zero_indegree)
    print("Random source node with in-degree zero:", source)
    print("=" * 165)
    return source
indegree_data = find_indegree(D1)
# do topological sort by Breadth First Search
def BST(D):
    source = pick_random_indegree_node(indegree_data)
    visited = set()
    visited.add(source)
    q = deque()
    q.append(source)
    topological_sorted = []
    while q :
        node = q.popleft()
        topological_sorted.append(node)
        for neighbor in D[node]:
            indegree_data[neighbor] -= 1
            if neighbor not in visited and indegree_data[neighbor] == 0:
                q.append(neighbor)
                visited.add(neighbor)
    print("Topological Sort Output : " , topological_sorted)
    print("=" * 165)
    return topological_sorted
BST(D1)