import graph.graph as gt
import graph.basicproblem as gb
V = [0, 1, 2, 3, 4, 5]
E = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 4),
     (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)}
Ew = {(1, 0, 1), (3, 0, 2), (5, 0, 3), (1, 1, 2), (2, 1, 4),
      (1, 2, 3), (2, 2, 5), (1, 3, 4), (3, 3, 5), (2, 4, 5)}
gt.draw_digraph(E)
[d, di, do] = gb.degree_set_w(V, Ew)
[Pc, Hx, Hy] = gb.craticalpath(V, Ew, di, do, V[0], V[-1])

# [V, Ec] = gb.graphw2graph(V, Pc)
# gt.draw_digraph(Ec)
print("Hx", Hx)
print("Hy", Hy)
print(Pc)
