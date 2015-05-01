import graph
from graph import *

# Computes the density of a subgraph given by a list of vertices
def density(g, verts):
	pass


# Finds the maximum density subgraph using Goldberg's algorithm
def max_density_subgraph(g):
	pass


# Prunes a graph based on local densities and returns a list of subgraphs
def prune_dense_graph(g):
	return []


def construct_network(g, guess):
	s = Vertex({})
	t = Vertex({})
	
	# for vert in g.vertices.keys():
		# s.add_neighbor(vert, )
		# vert.add_neighbor()
	


# Returns graph with vert1 and vert2 contracted into a single vertex
def contract(g, vert1, vert2):
	
	# Create the new contracted vertex
	new_vertex = Vertex(vert1.neighbors)
	for (vert, weight) in vert2.neighbors.items():
		new_vertex.inc_weight(vert, weight)
		# add weights of edges together
		# if vert in new_vertex.neighbors:
		# 	new_vertex.neighbors[vert] = weight + new_vertex.neighbors[vert]
		# else:
		# 	new_vertex.add_neighbor(vert,weight)
	
	# remove the self-edge
	if new_vertex.is_neighbor(vert1):
		new_vertex.del_neighbor(vert1)
	if new_vertex.is_neighbor(vert2):
		new_vertex.del_neighbor(vert2)
	
	# add the contracted vertices to the contracted list
	new_vertex.add_aux_info('contracted', [])
	if 'contracted' in vert1.aux:
		new_vertex.aux['contracted'] += vert1.aux['contracted']
	else:
		new_vertex.aux['contracted'].append(vert1)
	if 'contracted' in vert2.aux:
		new_vertex.aux['contracted'] += vert2.aux['contracted']
	else:
		new_vertex.aux['contracted'].append(vert2)
	
	# remove the two original vertices from the old vertex list
	new_verts = dict.copy(g.vertices)
	del new_verts[vert1]
	del new_verts[vert2]
	
	# make incoming edges point to new vertex
	for vert in new_verts:
		if vert.is_neighbor(vert1):
			vert.inc_weight(new_vertex, vert.neighbors[vert1])
			vert.del_neighbor(vert1)
		if vert.is_neighbor(vert2):
			vert.inc_weight(new_vertex, vert.neighbors[vert2])
			vert.del_neighbor(vert2)
	
	# add the new vertex
	new_verts[new_vertex] = 0
	
	return Graph(new_verts.keys())


# measures the connectedness of vert1 to the given set of vertices
def connectedness(vert_set, vert1):
	
	tot = 0
	
	for vert in vert_set:
		if vert.is_neighbor(vert1):
			tot += vert.neighbors[vert1]
	
	return tot


# returns the complement of the set of vertices A in the graph g's vertices
def complement(g, A):
	
	comp = set()
	
	for vert in g.vertices:
		if vert not in A:
			comp.add(vert)
	
	return comp


# returns the vertex in A complement that is most tightly connected to A
def most_tightly_connected(g, A):
	max_vert = (None, 0)
	
	for x in g.complement(A):
		c = connectedness(A, x)
		if c > max_vert[1]:
			max_vert = (x, c)
	
	return max_vert[0]


# returns the cut of the phase and the contracted graph
def min_cut_phase(g, a):
	
	A = set([a])
	
	while len(A) != len(g.vertices):
		
		x = most_tightly_connected(g, A)
		
		if len(A) == len(g.vertices) - 2:
			s = x
		
		if len(A) == len(g.vertices) - 1:
			t = x
			cut_phase = (A, g.complement(A))
		
		A.add(x)
	
	new_graph = contract(g, s, t)
	return (cut_phase, new_graph)


# calculates the weight of a cut
def weight_cut(g, cut):

	tot = 0

	for x in cut[0]:
		for (y, weight) in x.neighbors:
			if y in cut[1]:
				tot = tot + weight
	
	return tot


# Stoer-Wagner algorithm to find the minimum cut in an undirected graph
def min_cut_undir(g, a):
	
	new_graph = g
	min_cut = (None, float("inf"))

	while len(new_graph.vertices) > 1:
		
		(cut_phase, new_graph) = min_cut_phase(new_graph, a)
				
		if weight_cut(cut_phase) < min_cut[1]:
			min_cut = (cut_phase, weight_cut(cut_phase))
	
	return min_cut[0]


	