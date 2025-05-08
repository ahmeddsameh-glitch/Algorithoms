import heapq
from collections import defaultdict
#given graph
edges = [["a","b",4],["a","h",8],["b","c",8],["b","h",11],["c","d",7],["c","f",4],["c","i",2],
         ["d","e",9],["d","f",14],["e","f",10],["f","g",2],["g","h",1],["g","i",6],["h","i",7]]
no_of_vertexs = 9
# build our adjanency list
def build_adjacency_list(edges):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])  # undirected graph
    print("=" * 165)
    print("Adjacent List :\n", adj)
    print("=" * 165)
    return adj
# get the only known source in the given graph
def search_for_source(graph):
    # get first_node in the dictionary
    first_node = next(iter(graph))
    # [0] => first connected node , [1] =>  to choose weight
    lowest_weight = graph[first_node][0][1]
    for u in graph:
        for v,w in graph[u]:
            if w < lowest_weight:
                lowest_weight = w
                source = u
                next_source = v
    print("the source edge is :", source, "-", next_source ,"and the lowest weight of it is : ", lowest_weight)
    print("=" * 165)
    return [source,next_source,lowest_weight]

# applying Prim's Algorithom
def prim_mst(graph):
    # Initialize the priority queue
    priority_queue = []
    u,v,weight = search_for_source(adj_list)
    # Push the source edge into the priority queue
    heapq.heappush(priority_queue, (weight,u,v))
    visited = set()
    mst_edges = []
    min_cost = 0
    visited.add(u)
    no_of_edges = no_of_vertexs - 1
    i = 0
    while priority_queue and i <= no_of_edges :
        i+=1
        weight,u,v = heapq.heappop(priority_queue)
        print("current edge is : ",u, "-", v, ", and its weight is ", weight)
        if v in visited:
            continue
        # Add this edge to the MST
        visited.add(v)
        mst_edges.append([u,v,weight])
        min_cost += weight
        print("Vertex : " , v)

        for neighbor , weight_num in graph[v]:
            if neighbor not in visited:
                print(v , "-" , neighbor)
                heapq.heappush(priority_queue,(weight_num , v , neighbor))
        print("=" * 165)
        print("MST edges of the given graph : ", mst_edges)
        print("Min cost of the given graph : ", min_cost)
    return mst_edges , min_cost
adj_list = build_adjacency_list(edges)
prim_mst(adj_list)


