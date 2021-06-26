def Dijstra(V, E, v0):
    """给定V、E和起始顶点，给出最短路径长度"""
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

V = ['a', 'b', 'c', 'd', 'e', 'z']
E = {(4, 'a', 'b'), (2, 'a', 'd'), (3, 'b', 'c'), (3, 'b', 'e'),
     (2, 'c', 'z'), (3, 'd', 'e'), (1, 'e', 'z')}


# V = ['a', 'b', 'c']
# E = {(4, 'a', 'b'), (1, 'a', 'c'), (2, 'c', 'b')}


def is_same_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    lst1_clone = lst1[:]
    for i in lst2:
        lst1_clone.remove(i)

    if len(lst1_clone) == 0:
        return True
    else:
        return False

Dijstra(V, E, 'a')
