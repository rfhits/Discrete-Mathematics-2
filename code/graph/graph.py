import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# 此文件包含的方法有：
# draw方法
# 判断各种子图的方法
# 生成各种特殊的图的方法，如complete_set(n)


def draw_graph(E):
    '''通过边集，画无向图'''
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return


def draw_digraph(E):
    '''画有向图'''
    G = nx.DiGraph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return


def draw_weighted_graph(E):
    '''通过边集，画无向图'''
    G = nx.Graph()
    E_weight = [(e[1], e[2], e[0]) for e in E]
    G.add_weighted_edges_from(E_weight)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return

def Cartesianproduct(X, Y):
    XY = set({})
    for x in X:
        for y in Y:
            XY.add((x, y))
    return XY


def create_graph(m, n):
    """m个顶点的完全图，取n条边，随便画个图"""
    global V, XY
    V = range(m)
    XY = Cartesianproduct(V, V)
    E = random.sample(XY, n)
    return [V, E]


def is_subgraph(V, E, Vs, Es):
    '''判断是不是子图'''
    tv = (Vs <= V) and (Es <= E)
    return tv


def is_proper_subgraph(V, E, Vs, Es):
    '''判断真子图'''
    tv = ((Vs <= V) and (Es <= E)) and ((Vs < V) or (Es < E))
    return tv


def is_spanning_subgraph(V, E, Vs, Es):
    '''判断生成子图'''
    tv = ((Vs <= V) and (Es <= E)) and ((Vs == V) and (Es <= E))
    return tv


def is_induced_subgraph(V, E, Vs, Es):
    '''判断导出子图'''
    tv = ((Vs <= V) and (Es <= E))
    for (u, v) in E:
        # 对于E中的边而言，要么两端都在子图中，要么两端都不在子图中
        tv = tv and ((not((u in Vs) and (v in Vs))) or ((u, v) in Es))
    return tv


def complete_set(n):
    """生成完全图"""
    V = set({})
    E = set({})
    for i in range(n):
        V = V | {i}
        # V is a set, {1, 2, 3, 4, ..., n}
        for j in range(n):
            if(i < j):
                E = E | {(i, j)}
                # E = {(0, 1~n), (1, 2~n), ...}
    return (V, E)
# sample of complete_set
    # import graph.graph as gt
    # (V, E) = gt.complete_set(4)
    # V = {0, 1, 2, 3}
    # E = {(1, 2), (2, 3), (0, 3), (0, 2), (0, 1), (1, 3)}


def complete_set_another(n):
    V = set({})
    E = set({})
    for i in range(n):
        V.add(i)
        for j in range(n):
            if(i != j):
                E.add((i, j))
                # E = {(i, j): i, j = 0~n & i != j}
    return (V, E)


def connected_graph(V, E, V0, E0):
    """调用时，将E0赋值为E的第一条边，V0为E0的两个点"""
    # (u, v) = E[0]
    # E0 = {(u, v)}
    # V0 = {u, v}
    Vc = V0
    Ec = E0
    while E != set({}):
        n = len(Ec)  # 记录未进行子图扩展时，有几条边
        for (u, v) in E:    # 遍历原图的边，能添加，就添加
            if (u, v) not in Ec and (u in Vc or v in Vc):
                Vc = Vc | {u, v}
                Ec = Ec | {(u, v)}
        if len(Ec) == n:
            # 若遍历后，子图的边的数量不变，说明扩了相当于没扩展，可以退出
            break
    return [Vc, Ec]


def is_connected_graph(V, E):
    V = list(V)
    E = list(E)
    (u, v) = E[0]
    V0 = {u, v}
    E0 = {(u, v)}
    [Vc, Ec] = connected_graph(V, E, V0, E0)
    tv = (set(V) == set(Vc)) & (set(Ec) == set(E))
    return tv


def graph2array(V, E):
    n = len(V)
    A = np.zeros((n, n), dtype='int')
    A = np.array(A)
    for i in range(n):
        for j in range(n):
            if (i, j) in E:
                A[i, j] = 1
    return A


def degree_set(V, E):
    """给出每个点的度、入度和出度"""
    V = sorted(V)
    m = len(V)
    di = [0]*m
    do = [0]*m
    d = [0]*m
    for (u, v) in E:
        i = V.index(u)
        j = V.index(v)
        di[j] += 1
        do[i] += 1
        d[i] += 1
        d[j] += 1
    return [d, di, do]


def shortpath(V, E, di, Hx, path, zn):
    V = sorted(V)
    Pm = []
    for p in path:
        vn = p[-1]
        if vn == zn:
            Pm = Pm + [p]
            continue
        if di[V.index(vn)] != 0:
            Pm = Pm + [p]
            continue
        for (w, u, v) in E:
            if u == vn:
                kv = V.index(v)
                if di[kv] > 0:
                    di[kv] = di[kv]-1
                vw = p[0]+w
                if vw <= Hx[kv]:
                    Hx[kv] = vw
                    e = [vw] + p[1:] + [v]
                    Pm = Pm + [e]
    return [di, Hx, Pm]
