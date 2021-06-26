import networkx as nx
import matplotlib.pyplot as plt
import random

# 思路：
# 改写马老师的creat_graph函数，使之必然生成简单图
# 统计每个顶点的度数，并找出度数为奇数的顶点
# 因为某个定理的存在（见第一次作业），
# 度数为奇数的顶点个数一定是偶数
# 对于这些顶点，两两一组，
# 若之间有边，则删去，若之间无边，则连上

# 代码有个bug
# 在生成图的时候，保证是连通图
# 优先做连接，万不得已再删除
# 有度为1的顶点和一个度为奇数的顶点相连，删除此边将会导致孤立点。
# 解决：
# 找到一个度数≥2的顶点，然后奇数顶点就被转移了，
# 若无度数≥2的顶点，剩下的奇顶点个数大于1，必定有一个和此点不相连的奇顶点，可以连接

# 优点：很好理解
# 缺点：不能生成指定边数的欧拉图


def create_graph(m, n):
    """m个顶点的完全图，取n条边，随便画个图"""
    global V, XY
    V = range(m)
    XY = set({})
    for x in range(m):
        for y in range(x+1, m):
            XY.add((x, y))
    E = random.sample(XY, n)
    E = sorted(E)
    return [V, E]


def draw_graph(E):
    '''通过边集，画无向图'''
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return


def degree_set(V, E):
    """给出每个点的度"""
    V = sorted(V)
    m = len(V)
    d = [0]*m
    for (u, v) in E:
        i = V.index(u)
        j = V.index(v)
        d[i] += 1
        d[j] += 1
    return d


def is_simple_graph(E):
    """判断是不是简单图"""
    for e in E:
        if e[0] == e[1]:
            return False
        elif (e[1], e[0]) in E:
            return False
        else:
            pass
    return True


def get_odd_v(d):
    """得到顶点度数为奇数的list"""
    num_v = len(d)
    v_odd = []
    for i in range(num_v):
        if d[i] % 2 == 0:
            pass
        else:
            v_odd.append(i)
    return v_odd


def Euler_graph(V, E):
    """将一个简单图通过删边、加边的方式，变成欧拉图，并返回边集"""
    d = degree_set(V, E)
    v_odd = get_odd_v(d)
    n_v_odd = len(v_odd)  # 一定为偶数
    if n_v_odd == 0:
        pass
    else:
        for i in range(n_v_odd//2):
            # (u,v) 一前一后
            u = v_odd[i]
            v = v_odd[n_v_odd-i-1]
            if (u, v) in E:
                E.remove((u, v))
            elif (v, u) in E:
                E.remove((v, u))
            else:
                E.append((u, v))
    E = sorted(E)
    return E


num_v = 10
num_e = 30
[V, E] = create_graph(num_v, num_e)

print("E is simple graph?: ", is_simple_graph(E), "\n")

print("Edges:\n", E, "\n")
d = degree_set(V, E)
print("degree: ", d, "\n")

E_Euler = Euler_graph(V, E)

print("E_Euler:\n", E_Euler, "\n")
d = degree_set(V, E_Euler)
print("degree: ", d)

# draw_graph(E_Euler)
