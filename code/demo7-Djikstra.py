import graph.graph as gt
import graph.basicproblem as gb
V = ['a', 'b', 'c', 'd', 'e', 'z']
E = {(4, 'a', 'b'), (2, 'a', 'd'), (3, 'b', 'c'), (3, 'b', 'e'),
     (2, 'c', 'z'), (3, 'd', 'e'), (1, 'e', 'z')}
[d, di, do] = gb.degree_set_w(V, E)
print(d, di, do)
inf = 10000
Hx = [inf for x in range(len(V))]
Hx[0] = 0
path = [[0, 'a']]
print(di, Hx, path)
[di, Hx, path] = gb.short_path(V, E, di, Hx, path, 'z')
print(di, Hx, path)
[di, Hx, path] = gb.short_path(V, E, di, Hx, path, 'z')
print(di, Hx, path)
[di, Hx, path] = gb.short_path(V, E, di, Hx, path, 'z')
print(di, Hx, path)
