import cPickle as pickle
from graph import Vertex
from graph import Graph

v1 = Vertex({},{"name":"John"})
v2 = Vertex({v1:3},{"name":"Jane"})
v1.add_neighbor(v2,3)
v3 = Vertex({v2:2},{"name":"Charles"})
v2.add_neighbor(v3,2)
v4 = Vertex({v1:4,v2:2},{"name":"Catherine"})
v1.add_neighbor(v4,4)
v2.add_neighbor(v4,2)
v5 = Vertex({v1:9,v2:3,v3:8,v4:9},{"name":"Jessica"})
v1.add_neighbor(v5,9)
v2.add_neighbor(v5,3)
v3.add_neighbor(v5,8)
v4.add_neighbor(v5,9)
v6 = Vertex({v2:6,v3:10},{"name":"Hugo"})
v2.add_neighbor(v6,6)
v3.add_neighbor(v6,10)
v7 = Vertex({v5:2,v6:10},{"name":"Stanley"})
v5.add_neighbor(v7,2)
v6.add_neighbor(v7,10)
v8 = Vertex({v3:9,v7:3},{"name":"Emily"})
v3.add_neighbor(v7,9)
v7.add_neighbor(v7,3)

graph_var = Graph([v1,v2,v3,v4,v5,v6,v7,v8],[[0,1,0,1,1,0,0,0],[1,0,1,1,1,1,0,0],
[0,1,0,0,1,1,0,1],[1,1,0,0,1,0,0,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,0,1,0],
[0,1,1,0,0,0,1,0],[0,0,0,0,1,1,0,1],[0,0,1,0,0,0,1,0]])
pickle.dump(graph_var,open('test.p','wb'))