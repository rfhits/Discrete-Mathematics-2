import graph.graph as gt
m, n = 30, 20
[V, E] = gt.create_graph(m, n)
tv = gt.is_connected_graph(V, E)
gt.draw_graph(E)
print(V)
print(E)
print(tv)
(u, v) = list(E)[0]
V0 = {u, v}
E0 = {(u, v)}
[Vc, Ec] = gt.connected_graph(V, E, V0, E0)
tv = gt.is_connected_graph(Vc, Ec)
gt.draw_graph(Ec)
print(Vc)
print(Ec)
print(tv)
