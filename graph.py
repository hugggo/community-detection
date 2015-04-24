class Vertex:
	
	'''
	class fields:
		neighbors - a dictionary containing vertices as keys and the corresponding edge lengths as values
		auxiliary - a dictionary containing any auxiliary information about the vertex (i.e. 'name': 'Charles')
		degree - the out-degree of the vertex
	'''
	
	def __init__(self, neighbors={}, aux={}):
		self.neighbors = neighbors
		self.aux = aux
		self.degree = len(neighbors)
	
	# Adds an edge from self to neighbor to self's edge list
	def add_neighbor(self, neighbor, weight=1):
		self.neighbors[neighbor] = weight
		self.degree = self.degree + 1
	
	# Updates auxiliary information for field
	def add_aux_info(self, field, info):
		self.aux[field] = info
	
	# Deletes the edge from self to neighbor in self's edge list
	def del_neighbor(self, neighbor):
		del self.neighbors[neighbor]


class Graph:
	
	'''
	class fields:
		vertices - a dictionary containing the vertices in the graph and their corresponding indices in the adjacency matrix
	'''
	def __init__(self, vertices = {}, adjacency = []):
		if type(vertices) is list:
			self.vertices = {}
			ind = 0
			
			for vert in vertices:
				self.vertices[vert] = ind
				ind = ind + 1
			
			self.adj = self.__generate_adjacency()
		else
			self.vertices = vertices
			
			if adjacency == []:
				self.adj = self.__generate_adjacency()
			else:
				self.adj = adjacency
	
	def __generate_adjacency(self):
		pass
		
	
	
	
	

class NetworkFlow:
	
	def __init__(self, g, source, sink):
		self.graph = g
		self.s = source
		self.t = sink
	
	
	
	
