import graph.graph as gt
import graph.basicproblem as gb
V = ['a', 'b', 'c', 'd', 'e', 'z']
E = {(4, 'a', 'b'), (2, 'a', 'd'), (3, 'b', 'c'), (3, 'b', 'e'),
     (2, 'c', 'z'), (3, 'd', 'e'), (1, 'e', 'z')}
[Hx, Pm] = gb.shortest_path(V, E, V[0], V[-1])
print(V)
print(E)
print(Hx, Pm)
