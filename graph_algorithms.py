from graph import Graph
from collections import deque
import random


#######################################################################

def bfs_longest_path(graph: Graph, start: int) -> tuple[int, int]:
   
   distances = [-1] * graph.get_num_nodes()
   distances[start] = 0
   queue = deque([start])
    
   farthest_node = start
   max_distance = 0
    
   while queue:
      current = queue.popleft()
        
      for neighbor in graph.get_neighbors(current):
         if distances[neighbor] == -1:
            distances[neighbor] = distances[current] + 1
            queue.append(neighbor)
                
            
            if distances[neighbor] > max_distance:
               max_distance = distances[neighbor]
               farthest_node = neighbor
    
   return (farthest_node, max_distance)

#######################################################################

def get_diameter(graph: Graph) -> int:
   
    current_node = random.randint(0, graph.get_num_nodes() - 1)
    
    while True:
        
        next_node, current_length = bfs_longest_path(graph, current_node)
        
        new_node, new_length = bfs_longest_path(graph, next_node)
        
        if current_length == new_length: return current_length
            
        current_node = new_node
    
######################################################################

def get_clustering_coefficient(graph: Graph) -> float:

        
   remaining_neighbor = {v: set() for v in graph.vertices()}
   
   processed = set()     
   
   node_d = {}    
   d_nodes = {}

   for node in graph.vertices():
      
       d = len(graph.get_neighbors(node))
       node_d[node] = d
       
       if d in d_nodes: d_nodes[d].add(node)
       else: d_nodes[d] = {node}


   while len(processed) != graph.get_num_nodes():
       
       
       min_d = min(d_nodes.keys())
       
       current_node = d_nodes[min_d].pop()
       
      
       if len(d_nodes[min_d]) == 0: del d_nodes[min_d]

     
       neighbors = graph.get_neighbors(current_node)
       
       remaining_neighbors = set(neighbors) - processed
       
       for node in remaining_neighbors:
          
           curr_d = node_d[node]
           new_d = curr_d - 1
          
           d_nodes[curr_d].remove(node)
           
           if len(d_nodes[curr_d]) == 0: del d_nodes[curr_d]
           
           if new_d not in d_nodes: d_nodes[new_d] = set()
           
           d_nodes[new_d].add(node)
           node_d[node] = new_d

       
       processed.add(current_node)
       
       remaining_neighbor[current_node] = remaining_neighbors

  
   triangles = 0
   for node in remaining_neighbor:
       for i, m in enumerate(remaining_neighbor[node]):
           for n in list(remaining_neighbor[node])[i+1:]:
               if n in graph.get_neighbors(m): triangles += 1

 
   paths_of_length_2 = 0
   
   for vertex in graph.vertices():
       d = len(graph.get_neighbors(vertex))
       paths_of_length_2 += (d * (d - 1)) / 2

   if paths_of_length_2 == 0: return 0.0

   return (3 * triangles) / paths_of_length_2

#######################################################################

def get_degree_distribution(graph: Graph) -> dict[int, int]:
	distribution = {}

	for node in range(graph.get_num_nodes()):

		degree = len(graph.get_neighbors(node))
        
		if degree in distribution: distribution[degree] += 1
		else: distribution[degree] = 1
			
	return distribution

#######################################################################

