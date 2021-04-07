import graph.graph as gt
import graph.basicproblem as gb
V = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'}
E = {('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('h', 'i'), ('i', 'j'), ('j', 'k'), ('k', 'l'), ('l', 'm'), ('m', 'n'), ('n', 'o'), ('o', 'p'),
     ('p', 'q'), ('q', 'r'), ('r', 's'), ('s', 't'), ('a', 'n'), ('b', 'l'), ('c', 's'), ('d', 'k'), ('e', 'r'), ('f', 'j'), ('g', 'q'), ('h', 'o'), ('i', 'm'), ('p', 't'), ('t', 'a')}
Ea = gb.adjacentlist(V, E)
gt.draw_graph(E)
print("Ea", Ea)
