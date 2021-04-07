import graph.graph as gt
import graph.basicproblem as gb
# V = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
# E = {('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('h', 'i'), ('i', 'j'), ('j', 'k'), ('k', 'l'), ('l', 'm'), ('m', 'n'), ('n', 'o'), ('o', 'p'),
#      ('p', 'q'), ('q', 'r'), ('r', 's'), ('s', 't'), ('a', 'n'), ('b', 'l'), ('c', 's'), ('d', 'k'), ('e', 'r'), ('f', 'j'), ('g', 'q'), ('h', 'o'), ('i', 'm'), ('p', 't'), ('t', 'a')}


# P212, 7, (b) hamilton?
# V = [1, 2, 3, 4, 5, 6]
# E = {(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (1, 6), (3, 5), (3, 6)}

# P212, 7, (d) hamilton?
# V = [1, 2, 3, 4, 5, 6, 7, 8]
# E = {(1, 2), (1, 6), (2, 3),(2, 5), (2, 7), (3, 4),(3, 8), (4, 5), (5, 6), (5, 8), (6, 7)}

V = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
E = {('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a'), ('a', 'f'), ('b', 'g'),
     ('c', 'h'), ('d', 'i'), ('e', 'j'), ('f', 'h'), ('g', 'i'), ('h', 'j'), ('i', 'f'), ('j', 'g')}

filename = "19231188_homework3_t3.txt"
f = open(filename, "w")
v0 = "d"
paths = gb.Hamiltonpath(V, E, v0)
for path in paths:
     string = str(path)
     print(string[1:-1], file=f)
print(len(paths))

# gt.draw_graph(E)
