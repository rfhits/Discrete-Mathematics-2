import graph.graph as gt
import graph.basicproblem as gb
V = ['a', 'b', 'c']
E = {(1, 'a', 'b'), (1, 'b', 'c'), (3, 'a', 'c')}
[Hx, Pm] = gb.shortest_path(V, E, V[0], V[-1])
print(V)
print(E)
print(Hx, Pm)
