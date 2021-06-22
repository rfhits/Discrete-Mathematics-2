import math


def degree_set_w(V, E):
    """给出每个点的度、入度和出度"""
    V = sorted(V)
    m = len(V)
    di = [0]*m
    do = [0]*m
    d = [0]*m
    for (w, u, v) in E:
        i = V.index(u)
        j = V.index(v)
        di[j] += 1
        do[i] += 1
        d[i] += 1
        d[j] += 1
    return [d, di, do]


def set2V(E):
    """从边集产生点集"""
    V = set({})
    for (u, v) in E:
        V = V | {u, v}
    return V


def subEulercircuit(E, v0):
    """从一点出发，找到一条回路，返回点顺序和使用的边"""
    circuit = tuple([v0])
    S = set({})
    while (circuit[0] != circuit[-1] or len(circuit) == 1):
        y = circuit[-1]
        for (u, v) in E:
            if(u == y):
                circuit = circuit+tuple([v])
                E = E-{(u, v)}
                S = S | {(u, v)}
                break
    return [circuit, S]


def Eulercircuit(E, v0):
    """给出欧拉回路"""
    [circuit, S] = subEulercircuit(E, v0)
    E = E-S
    while (E != set({})):
        V1 = set(circuit)
        V2 = set2V(E)
        V1V2 = V1 & V2
        # 已有回路和整个图的公共点集
        for v0 in V1V2:
            # 从公共点集，生成回路点集和边
            [subcircuit, S] = subEulercircuit(E, v0)
            if S == set({}):
                continue
            k = circuit.index(v0)
            circuit = circuit[0:k]+subcircuit + \
                circuit[k+1:-1]+tuple([circuit[-1]])
            E = E-S
            break
    return circuit


def adjacentlist(V, E):
    """given vetice and edges,
    
    return adjacent list
    
    return type like:

    [ [1,[2,3]], [2, [3]], [3,[1,2]] ]
    """
    Ea = []
    for w in V:
        e0 = [w]
        e1 = []
        for (u, v) in E:
            if u == w and (v not in e1):
                e1 = e1+[v]
            if v == w and (u not in e1):
                e1 = e1+[u]
        e0 = e0+[sorted(e1)]
        Ea = Ea+[e0]
    return sorted(Ea)


def tourpath0(V, E, path, m):
    """given vertex set, adjacent list, path
    
    尽量使用邻接表中靠前的点，走出一条尽可能长的path 
    """
    while(len(path) < m):
        w = path[-1]
        i = V.index(w)
        E1 = E[i]
        E2 = E1[1] # 该点所对应的邻接点的集合
        for u in E2:
            if(u not in path):
                path.append(u)
                break
        if(path[-1] == w):
            break
    return path


def tourpath1(V, E, path, m):
    """末尾点走不下去了，据末尾点在倒数第二个点邻接表中的index，换后面的点再走。"""
    v = path.pop()
    while(len(path) != 0):
        u = path[-1]
        i = V.index(u)
        E1 = E[i]
        E2 = E1[1]
        k = E2.index(v)
        while(k < (len(E2)-1)):
            k = k+1
            v = E2[k]
            if(v not in path):
                path.append(v)
                break
        if(u != path[-1]):
            break
        v = path.pop()
    return path


def tourpath(V, E, path, m):
    if(len(path) == m):
        path = tourpath1(V, E, path, m)
    while(len(path) != 0):
        path = tourpath0(V, E, path, m)
        if(len(path) == m):
            break
        path = tourpath1(V, E, path, m)
    return path


def Hamiltonpath(V, E, v0):
    global Ea, paths
    V = sorted(V)
    Ea = adjacentlist(V, E)
    paths = set({})
    path = [v0]
    m = len(V)
    path = tourpath(V, Ea, path, m)
    paths = paths | {tuple(path)}
    while(len(path) == m):
        path = tourpath(V, Ea, path, m)
        if len(path) == m:
            paths = paths | {tuple(path)}
            print(path)
    return paths


def short_path(V, E, di, Hx, path, zn):

    # Hx就是记录V[0]和其他点之间距离的list

    #     对于所有路径p
    # vn是路径p的最后顶点
    # 若vn不是终止顶点
    # 对于所有边(u,v,d)∈E
    # 若u==vn
    # 求新顶点距离vd
    # if vd<=Hx[kv]
    #         增加新顶点v

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


def shortest_path(V, E, v0, vn):
    V = sorted(V)
    [d, di, do] = degree_set_w(V, E)
    Pm0 = []
    Pm = [[0, v0]]
    inf = 10000
    Hx = [inf for x in range(len(V))]
    # Hx就是记录V[0]和其他点之间距离的list
    Hx[0] = 0
    while Pm0 != Pm:
        # 知道某次操作，Pm0和Pm不变
        Pm0 = Pm
        [di, Hx, Pm] = short_path(V, E, di, Hx, Pm0, vn)
    Pm = sorted(Pm)
    return [Hx, Pm]


def Huffmantree(W):
    """W=[['A',0.08], ['B',0.1], ['C',0.12]]"""
    W0 = []
    for [a, w] in W:
        W0 = W0+[[w, a]]
    tree = sorted(W0)
    while len(tree) != 1:
        w = tree[0][0]+tree[1][0]
        w = math.floor(w*10000)/10000
        tree = [[w, tree[0], tree[1]]]+tree[2:]
        tree = sorted(tree)
    return tree[0]


def huffmancoding(subtree, code):
    if len(subtree) == 2:
        return [[subtree[1], code]]
    else:
        node0 = subtree[1]
        node1 = subtree[2]
        code = huffmancoding(node0, code+'0')+huffmancoding(node1, code+'1')
        return code


def HuffmanCoding(tree):
    code0 = huffmancoding(tree[1], '0')
    code1 = huffmancoding(tree[2], '1')
    return code0+code1


W = [['A', 0.4], ['B', 0.1], ['C', 0.2], ['D', 0.15], ['E', 0.15]]
tree = Huffmantree(W)
C = HuffmanCoding(tree)
print(C)


def Prim_span_tree(V, E):
    """given [V_list, E_list],
        return [V_list, E_list]"""
    E = sorted(E)
    [w, u, v] = E[0]
    Vt = {u, v}
    Et = {(w, u, v)}
    del E[0]
    n = len(V)
    while (len(Et) < (n-1)):
        i = 0
        while(i < len(E)):
            [w, u, v] = E[i]
            if (u in Vt and v not in Vt) or (u not in Vt and v in Vt):
                Et = Et | {(w, u, v)}
                Vt = Vt | {u, v}
                del E[i]
                break
            i = i+1
    return [Vt, Et]


def is_cycled(V, E, u0, v0):
    tv = False
    Vc = {u0, v0}
    Ec = {(u0, v0)}
    n = 0
    while(n != len(Vc)):
        n = len(Vc)
        for (w, u, v) in E:
            if((u in Vc) and (v in Vc)):
                tv = True
                return tv
            if (u in Vc and v not in Vc) or (u not in Vc and v in Vc):
                Ec = Ec | {(u, v)}
                Vc = Vc | {u, v}
                E = E-{(w, u, v)}
                break
    return tv


def Kruskal_span_tree(V, E):
    E = sorted(E)
    Vt = set({})
    Et = set({})
    n = len(V)
    k = 0
    i = 0
    while(len(Et) < n-1):
        [w, u, v] = E[i]
        i = i+1
        if(((u in Vt) and (v in Vt))):
            if(is_cycled(Vt, Et, u, v)):
                continue
        Et = Et | {(w, u, v)}
        Vt = Vt | {u, v}
    return [Vt, Et]
