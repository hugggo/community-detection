import graph

class User(graph.Vertex):
	
	def __init__(self, name=''):
		graph.Vertex.__init__(self)
		self.add_aux_info('name', name)
	
	def get_friends(self):
		return self.neighbors
	
	def add_friend(self, friend, closeness=None):
		self.add_neighbor(friend, closeness)
	
	def get_closeness(self, friend):
		return None

