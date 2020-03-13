def tobin(n,pre):
    res = []
    while n//2 > 0:
        res.append(n%2)
        n = n // 2
    res.append(n)
    res.reverse()
    return [0]*(pre-len(res)) + res

def BFS(G,C,s,t):
    parent = {}
    distance = {}
    for i in range(len(G)):
        parent[i] = None
        distance[i] = float('inf')
    distance[s] = 0

    Q,i = [s],0

    while i<len(Q):
        u = Q[i]
        for v in G[u]:
            if distance[v] == float('inf') and C[(u,v)]>0:
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.append(v)
        i+=1
    if parent[t] == None:
        return [],0
    path = []
    cur = t
    cap = float('inf')
    while parent[cur] != None:
        path.append((parent[cur],cur))
        cap = min(cap,C[(parent[cur],cur)])
        cur = parent[cur]
    path.reverse()
    return path,cap
   
def FordFulkerson(G,E,Gf,Ef,s,t):
    while True:
        path,cap = BFS(Gf,Ef,s,t)
        if cap == 0:
            break
        for e in path:
            u,v = e
            if (u,v) in E:
                E[(u,v)][1] += cap
            else:
                E[(v,u)][1] -= cap
            Ef[(u,v)]-=cap
            Ef[(v,u)]+=cap
    f = 0
    for v in G[s]:
        f += E[(s,v)][1]
    return f

def BinaryCap(C):
    MaxCap = -float('inf')
    for e in C:
        MaxCap = max(MaxCap,C[e])
    pre = len(tobin(MaxCap,0))
    E = {}
    for e in C:
        E[e] = tobin(C[e],pre)
    return E,pre

def Initialize(G,C):
    BinCap, pre = BinaryCap(C)
    E = {}
    for e in C:
        E[e] = [C[e],0]
    Gf = [[] for _ in range(len(G))]
    Ef = {}
    for u in range(len(G)):
        for v in G[u]:
            Gf[v].append(u)
            Gf[u].append(v)
            Ef[(u,v)] = BinCap[(u,v)][0]
            Ef[(v,u)] = 0
    return BinCap, pre, E, Gf, Ef

def CapacityScaling(G,C,s,t):
    BinCap, pre, E, Gf, Ef = Initialize(G,C)
    
    for i in range(pre):
        for e in Ef:
            if e not in C:
                Ef[e] = Ef[e]*2
            elif e in C and i == 0:
                Ef[e] = BinCap[e][i]
            else:
                Ef[e] = Ef[e]*2 + BinCap[e][i]
                E[e][1]*=2
        f = FordFulkerson(G,E,Gf,Ef,s,t)
    return f

G = [[1,2],[3],[1,4],[2,5],[3,5],[]]
C = {
        (0,1):16,
        (0,2):13,
        (1,3):12,
        (2,1):4,
        (2,4):14,
        (3,2):9,
        (3,5):20,
        (4,3):7,
        (4,5):4
    }

#print(CapacityScaling(G,C,0,5))

        
    
