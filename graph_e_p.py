import heapq

class Node:
    def __init__(self, weight):        
        self.dist = float('inf')
        self.prev = None #undeclared path
        self.adj = None #undeclared adjacency node array
        self.prob = None # undeclared adjacency weight array for probablity
        self.expect = None #undlecared adjacency weight array for expected value. 
        self.weight = weight #initial weight value for the edge. 


""" Example of Node that is converted:

node_a = Node(weight):
    self.dist = 0
    self.prev = None
    self.adj = [node1, node2,...]
    self.prob = [weight_1,weight_2,...] # value at for each edge to get to the node in adjacency. 
    self.expect = [weight_1,weight_2,...] # same as prob. 
    self.weight = weight            
"""    
# min heap is initialized, and the minimum value is based off the Node.dist value within the node. So the smallest distance is popped from the heap first.   \
min_heap = []

def convert_graph(root_node):
    root_node.dist = 0
    root_node.prev = None
    for i in range(len(nodes.adj)):
        nodes.adj[i].dist = float('inf')
        nodes.adj[i].prev = None        
        
    BFS Traversal:
        parent_node # node that previously called this node. 
        for i in range(len(nodes.adj)): #look at adjancency in each node. 
            if nodes.adj[i] is not parent_node: #don't alter the parent node. 
                nodes.adj[i].dist = float('inf')  # set value to infinity at each node
                nodes.adj[i].prev = None          #set previous to each node equal none. 
                nodes.expect[i] += nodes.weight   #add the node weight to the expected value. 
                nodes.prob[i] = 1-(1-nodes.weight)(1-nodes.prob[i]) # calculate the new probability based upon derivation below.. 
                min_heap.insert(nodes) #insert the node
   
           
def solve_sssp_expected(root_node):
    for i in range(len(root_node.adj)):
        relax(root_node, root_node.adj[i], root_node.prob[i]  )
    while min_heap: # if there is min heap this will keep going. 
        curr_node = min_heap.heappop()  #accesses the smallest node. 
        for i in range(len(curr_node.adj)):
            future_e_val = curr_node.prob[i] + curr_node.prob
            if curr_node.adj[i].dist > future_e_val : #if the node checking is a longer path, relax it
                relax(curr_node, curr_node.adj[i], curr_node.prob[i] + curr_node.prob )
        
def solve_sssp_probability(graph_g):
    for i in range(len(root_node.adj)):
        relax(root_node, root_node.adj[i], 1- root_node.prob[i]  )  
        
    while min_heap:# if there is min heap this will keep going. 
        curr_node = min_heap.heappop()  #accesses the smallest node. 
        for i in range(len(curr_node.adj)):
            p_no_dementor = 1-curr_node.prob # since probability of at least one one demtrantor is saved, find the probability of no dementor
            p_new = p_no_dementor*(1-curr_node.prob[i]) #multiply p_no_dem by probability of no dementor for the next path. 
            if curr_node.adj[i].dist > p_new : #if the node checking is a longer path, relax it
                relax(curr_node, curr_node.adj[i], p_new)
           

def relax(curr_node, called_node, new_d):     
    curr_node.prev = called_node                          # change the declared previous node from None to called_node
    curr_node.dist = new_d                                # change the weight from infinity to actual distnace. 
    min_heap.insert(curr_node)                            # insert to heap. 
   
if __name__ == "__main__":   
    convert_graph(root_node)
    solve_sssp_expected(graph_g)
    solve_sssp_probability(graph_g)
