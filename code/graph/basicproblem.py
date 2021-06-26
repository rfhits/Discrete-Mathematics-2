import math


def degree_set_w(V, E):
    """
    给出每个点的度、入度和出度

    Example
    ---
    return: \n
    [\n
    d = [2,3,4],\n
    d_in = [1,2,2],\n
    d_out = [1,2,2]\n
    ]
    """
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
        E2 = E1[1]  # 该点所对应的邻接点的集合
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
    """我记得马殿富这个代码是错的，慎用"""

    # Hx就是记录V[0]和其他点之间距离的list
    # 对于所有路径p
    # vn是路径p的最后顶点
    # 若vn不是终止顶点
    # 对于所有边(u,v,d)∈E
    # 若u==vn
    # 求新顶点距离vd
    # if vd<=Hx[kv]
    # 增加新顶点v

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
    """我记得马殿富这个代码错的，慎用"""
    V = sorted(V)
    [d, di, do] = degree_set_w(V, E)
    Pm0 = []
    Pm = [[0, v0]]
    inf = 10000
    Hx = [inf for x in range(len(V))]
    # Hx就是记录V[0]和其他点之间距离的list
    Hx[0] = 0
    while Pm0 != Pm:
        # 直到某次操作，Pm0和Pm不变
        Pm0 = Pm
        [di, Hx, Pm] = short_path(V, E, di, Hx, Pm0, vn)
    Pm = sorted(Pm)
    return [Hx, Pm]


def Dijstra(V, E, v0):
    """给定V、E和起始顶点，给出最短路径长度

    我自己写的，应该对的"""
    # Dst表示distance dict，
    # v0到各个顶点目前已知的距离，初始化为infty
    # N表示已经被确认是最短距离的那些点

    # 在Dst中选一个最小的点（此点不在N中）
    # 然后添加到N中，并且更新Dst
    if v0 not in V:
        print("the vertex not in Graph")
        return
    N = []
    inf = 10000
    Dst = dict()
    for v in V:
        Dst[v] = inf
    Dst[v0] = 0
    sortedDst = None
    ancher = None
    while sorted(N) != sorted(V):
        sortedDst = sorted(Dst.items(), key=lambda x: x[1])
        # 这一段循环，只是为了找到目前距离最小且未被添加进N的点
        for (v, d) in sortedDst:
            if v in N:
                pass
            else:
                # 成功拿到第一个不在N中，并且dst最小的v
                # 取名为anchor
                N.append(v)
                ancher = v
                break

        # 根据edges刷新Dst
        for (w, x, y) in E:
            if x == ancher and w + Dst[x] < Dst[y]:
                Dst[y] = w + Dst[x]
            elif y == ancher and w + Dst[y] < Dst[x]:
                Dst[x] = w + Dst[y]
            else:
                pass
    print(Dst)
    return Dst


def stepu0v(di0, E):
    """given know early_finished_time vetices and edges, return avaible edges"""
    S = set({})
    for u0 in di0:
        for (w, u, v) in E:
            if u == u0:
                S = S | {(w, u, v)}
    return S


def stepuv0(do0, E):
    S = set({})
    for v0 in do0:
        for (w, u, v) in E:
            if v == v0:
                S = S | {(w, u, v)}
    return S


def TEpath(S, Hx, di):
    di0 = set({})
    for (w, u, v) in S:
        if Hx[v] < Hx[u]+w:
            Hx[v] = Hx[u]+w
        if di[v] > 0:
            di[v] = di[v]-1
        if di[v] == 0:
            di0 = di0 | {v}
    return [Hx, di, di0]


def TLpath(S, Hy, do):
    do0 = set({})
    for (w, u, v) in S:
        if Hy[u] > Hy[v]-w:
            Hy[u] = Hy[v]-w
        if do[u] > 0:
            do[u] = do[u]-1
        if do[u] == 0:
            do0 = do0 | {u}
    return [Hy, do, do0]


def craticalTE(V, E, di, v0, vn):
    Hx = [0]*len(V)  # time list

    di0 = {v0}
    while vn not in di0:
        S = stepu0v(di0, E)
        [Hx, di, di0] = TEpath(S, Hx, di)
        E = E-S
    return Hx


def craticalTL(V, E, do, Hn, v0, vn):
    Hy = [1000]*len(V)
    Hy[len(V)-1] = Hn
    do0 = {vn}
    while v0 not in do0:
        S = stepuv0(do0, E)
        [Hy, do, do0] = TLpath(S, Hy, do)
        E = E-S
    return Hy


def craticalpath(V, E, di, do, v0, vn):
    Hx = craticalTE(V, E, di, v0, vn)
    Hn = Hx[len(V)-1]
    Hy = craticalTL(V, E, do, Hn, v0, vn)
    V = list(V)
    N = len(V)
    C = set({})
    for k in range(N):
        if Hx[k] == Hy[k]:
            C = C | {V[k]}
    Pc = set({})
    for (w, u, v) in E:
        if u in C and v in C:
            Pc = Pc | {(w, u, v)}
    return [Pc, Hx, Hy]


def graph2tree(V, E):
    E = sorted(E)
    (u, v) = E[0]
    Vt = {u, v}
    Et = {(u, v)}
    E = set(E)
    n = len(V)
    while(len(Et) < (n-1)):
        m = len(Vt)
        for (u, v) in E:
            if((u in Vt and v not in Vt)
               or (u not in Vt and v in Vt)):
                Vt = Vt | {u, v}
                Et = Et | {(u, v)}
        E = E-Et
        if(m == len(Vt)):
            break
    return [Vt, Et]


def is_tree(V, E):
    tv = True
    E = sorted(E)
    (u, v) = E[0]
    Vt = {u, v}
    E = set(E)-{(u, v)}
    Et = {(u, v)}
    while(E != set({})):
        for (u, v) in E:
            if (u in Vt) and (v in Vt):
                tv = False
                break
            if ((u in Vt) and (v not in Vt)) or ((u not in Vt) and (v in Vt)):
                Vt = Vt | {u, v}
                E = E-{(u, v)}
                Et = Et | {(u, v)}
        if(tv == False):
            break
    if((len(Vt)-1) != len(Et)):
        tv = False
    return tv


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
