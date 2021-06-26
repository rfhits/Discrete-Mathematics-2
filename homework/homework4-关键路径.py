v2EFT = dict()
v2LFT = dict()

def get_EFT(v, Ew):
    if v in v2EFT.keys():
        return v2EFT[v]
    
    u_list = []
    t_list = []
    for e in Ew:
        # e = (w, u, v)
        if e[2] == v:
            u_list.append(e[1])
            t_list.append(e[0])
    u2t = dict()
    for i in range(len(u_list)) :
        u2t[u_list[i]] = t_list[i]
    
    v_EFT = max([(get_EFT(u, Ew) + u2t[u]) for u in u_list])
    v2EFT[v] = v_EFT
    return v_EFT

def get_LFT(u, Ew):
    if u in v2LFT.keys():
        return v2LFT[u]
    
    v_list = []
    t_list = []
    # u -w-> v
    for e in Ew:
        # [w, u, v]
        if e[1] == u :
            v_list.append(e[2])
            t_list.append(e[0])

    v2t = dict()
    for i in range(len(v_list)) :
        v2t[v_list[i]] = t_list[i]

    u_LFT = min([(get_LFT(v,Ew)-v2t[v]) for v in v_list])
    v2LFT[u] = u_LFT
    return u_LFT




V = [0, 1, 2, 3, 4, 5]
E = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 4),
     (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)}
Ew = {(1, 0, 1), (3, 0, 2), (5, 0, 3), (1, 1, 2), (2, 1, 4),
      (1, 2, 3), (2, 2, 5), (1, 3, 4), (3, 3, 5), (2, 4, 5)}


v0 = V[0]
vn = V[-1]

v2EFT[v0] = 0
v2LFT[vn] = get_EFT(V[-1], Ew)
get_LFT(V[0], Ew)

