import graph.graph as gt
import graph.basicproblem as gb
V = {0, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}
E = {(0, 8), (0, 10), (2, 3), (3, 4), (4, 9), (6, 0), (8, 9),
     (9, 6), (9, 10), (10, 2), (10, 14), (12, 13), (13, 14),
     (14, 12), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 0)}

[d, di, do] = gt.degree_set(V, E)
circuit = gb.Eulercircuit(E, 0)
print(d)
print(circuit)
gt.draw_graph(E)
