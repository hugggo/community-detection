import graph
from graph import *
import copy

# Computes the density of a subgraph given by a list of vertices
def density(g, verts):
	pass

# Finds the maximum density subgraph using Goldberg's algorithm
def max_density_subgraph(g):
	pass

# Prunes a graph based on local densities and returns a list of subgraphs
def prune_dense_graph(g):
	return []

# Returns graph with vert1 and vert2 contracted into a single vertex
def contract(g, vert1, vert2) :
	
	# Create the new contracted vertex
	new_vertex = Vertex(vert2.neighbors)
	for (vert, weight) in vert1.neighbors.items():
		if vert in new_vertex.neighbors:
			new_vertex.neighbors[vert] = weight + new_vertex.neighbors[vert]
		else:
			new_vertex.add_neighbor(vert,weight)
	if vert1 in new_vertex.neighbors:
		del new_vertex.neighbors[vert1]
	if vert2 in new_vertex.neighbors:
		del new_vertex.neighbors[vert2]
	
	
	new_verts = dict.copy(g.vertices)
	del new_verts[vert1]
	del new_verts[vert2]
	new_verts[new_vertex] = 0

	
	return Graph(new_verts.keys())
	

def connectedness(vertlist, vert1):
	sum = 0
	for vert in vertlist.neighbors.keys():
		if vert1 in vert.neighbors:
			sum = sum + vert.neighbors[vert1]
	return sum

def complement (g, A):
	returnlist = {}
	for vert in g.vertices:
		if not(vert in A):
			returnlist[vert] = 0
	return returnlist


def min_cut_phase (g, a):
	A = a
	while len(A) != len(g.vertices):
		maxvert = g.vertices.keys()[0]
		maxval = 0
		for x in g.vertices.keys():
			if x not in A and connectedness(A, x) > maxval:
				maxvert = x
				maxval = connectedness(A,x)
		if len(A) == len(g.vertices) - 2:
			vert1 = x
		if len(A) == len(g.vertices) - 1:
			vert2 = x
			cutphase = (A, complement(g, A))
		A[x] = 0
	newgraph = contract(g, vert1, vert2)
	return (cutphase, newgraph)

def weight_cut (g, cutphase):
	(A, Aprime) = cutphase
	sum = 0
	for x in A:
		sum = sum + connectedness(x, Aprime)
	return sum

def min_cut (g, a):
	A = a
	while len(g.vertices) > 1:
		(cutphase, newgraph) = min_cut_phase(g, a)
		mincut = None
		minval = float("inf")
		if weight_cut(cutphase) < minval:
			mincut = cutphase
			minval = weight_cut(cutphase)
	return mincut


	