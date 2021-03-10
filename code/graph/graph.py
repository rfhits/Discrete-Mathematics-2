import networkx as nx
import matplotlib.pyplot as plt

# 此文件包含的方法有：
# draw方法
# 判断各种子图的方法
# 生成各种特殊的图的方法，如complete_set(n)


def draw_graph(E):
    '''画无向图'''
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
