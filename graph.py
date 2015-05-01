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
		self.degree += 1
	
	# Updates auxiliary information for field
	def add_aux_info(self, field, info):
		self.aux[field] = info
	
	# Deletes the edge from self to neighbor in self's edge list
	def del_neighbor(self, neighbor):
		del self.neighbors[neighbor]
		
	# Increases weight between self and neighbor
	def inc_weight(self, neighbor, weight=1):
		if neighbor in self.neighbors:
			self.neighbors[neighbor] += weight
		else:
			self.add_neighbor(neighbor, weight)
	
	def is_neighbor(self, neighbor):
		return neighbor in self.neighbors


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
				ind += 1
			
			# self.adj = self.__generate_adjacency()
		else:
			self.vertices = vertices
			
			# if adjacency == []:
			# 	self.adj = self.__generate_adjacency()
			# else:
			# 	self.adj = adjacency
		
		self.adj = self.__generate_adjacency()
		
		self.num_verts = len(self.vertices)
		self.num_edges = sum(map(lambda x: len(x.neighbors), self.vertices.keys()))
	
	def __generate_adjacency(self):
		adjacency = [[0 for i in range(len(self.vertices))] for j in range(len(self.vertices))]
		
		for vert in self.vertices.keys():
			for (neighbor,dist) in vert.neighbors.items():
				adjacency[self.vertices[vert]][self.vertices[neighbor]] = dist
		
		return adjacency
	
	# returns the complement of the set of vertices A in the graph g's vertices
	def complement(self, A):
		
		comp = set()
		
		for vert in self.vertices:
			if vert not in A:
				comp.add(vert)
		
		return comp
	
		
		
	
	
	
	

class NetworkFlow:
	
	def __init__(self, g, source, sink):
		self.graph = g
		self.s = source
		self.t = sink
		self.flow = [[0 for i in range(len(g.vertices))] for j in range(len(g.vertices))]
	
	# Finds an augmenting path
	def aug_path(self, cur, path):
		
		if cur == self.t:
			return path
		
		for vert in self.graph.vertices.keys():
			
			if vert not in path and self.graph.adj[self.graph.vertices[cur]][self.graph.vertices[vert]] > self.flow[self.graph.vertices[cur]][self.graph.vertices[vert]]:
				result = self.aug_path(vert, path + [vert])
				
				if result != None:
					return result

		# for (vert, cap) in cur.neighbors.items():
			
		# 	if vert not in path and cap > self.flow[self.graph.vertices[cur]][self.graph.vertices[vert]]:
		# 		result = self.aug_path(vert, path + [vert])
				
		# 		if result != None:
		# 			return result
	
	
	# finds the maximum flow and a minimum cut using Ford-Fulkerson
	def ford_fulkerson(self):
		
		path = self.aug_path(self.s, [self.s])
		
		while path != None:
			
			residuals = []
			
			for i in range(len(path)-1):
				residuals.append(self.graph.adj[self.graph.vertices[path[i]]][self.graph.vertices[path[i+1]]] - self.flow[self.graph.vertices[path[i]]][self.graph.vertices[path[i+1]]])
			
			flow = min(residuals)
			
			for i in range(len(path)-1):
				self.flow[self.graph.vertices[path[i]]][self.graph.vertices[path[i+1]]] += flow
				self.flow[self.graph.vertices[path[i+1]]][self.graph.vertices[path[i]]] -= flow
			
			path = self.aug_path(self.s, [self.s])
		
		cut_s = set()
		queue = [self.s]
		while len(queue) > 0:
			
			cur = queue.pop()
			cut_s.add(cur)
			
			for vert in self.graph.vertices.keys():
				if vert not in cut_s and vert not in queue and self.graph.adj[self.graph.vertices[cur]][self.graph.vertices[vert]] > self.flow[self.graph.vertices[cur]][self.graph.vertices[vert]]:
					queue.append(vert)
		
		cut_t = self.graph.complement(cut_s)
		
		return (sum(self.flow[self.graph.vertices[self.s]]), (cut_s, cut_t))
			
			
		
		
			
					
	
	
