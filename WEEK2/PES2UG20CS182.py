
import queue
import copy
from collections import deque

def A_star_Traversal(cost, heuristic, start_point, goals):
	#TODO
    path = []
    n = len(cost)                                               
    explored = [0 for i in range(n)]                             
    p_queue = queue.PriorityQueue()             

    p_queue.put((heuristic[start_point], ([start_point], start_point, 0)))

    while(p_queue.qsize() != 0):

        est_cost, s_node = p_queue.get()
        path = s_node[0]
        node = s_node[1]
        node_cost = s_node[2]

        if explored[node] == 0:
            explored[node] = 1

            if node in goals:
                return path

            for i in range(1, n):
                if cost[node][i] > 0 and explored[i] == 0:

                    final_cost = node_cost + cost[node][i]
                    et_cost = final_cost + heuristic[i]

                    p_neigh = copy.deepcopy(path)
                    p_neigh.append(i)
                    
                    p_queue.put((et_cost, (p_neigh, i, final_cost)))

    return list()

def neighb(adjList):
    neighbourList = []

    for index, node in enumerate(adjList[1::], start=1):

        if node > 0:
            neighbourList.append(index)

    return neighbourList[::-1]

def DFS_Traversal(cost, start_point, goals):
    st = deque()
    st.append({
        "node": start_point,
        "path": [start_point]
    })
    visited_nodes = set()
    while (st):
        p_node = st.pop()

        if p_node["node"] in visited_nodes:
            continue

        visited_nodes.add(p_node["node"])

        if(p_node["node"] in goals):
            return p_node["path"]

        neighb_pop_nd = neighb(cost[p_node["node"]])

        for nodes in neighb_pop_nd:
            if nodes not in visited_nodes:
                node_rec = {
                    "node": nodes,
                    "path": p_node["path"] + [nodes]
                }
                st.append(node_rec)

    return []
    # TODO
   
