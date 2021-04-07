import graph.graph as gt
m, n = 8, 20
[V, E] = gt.create_graph(m, n)
gt.draw_graph(E)
print(V)
print(E)
A = gt.graph2array(V, E)
print(A)
