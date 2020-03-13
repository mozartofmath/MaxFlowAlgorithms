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
   
def FordFulkerson(G,C,s,t):
    E = {}
    for e in C:
        E[e] = [C[e],0]
    Gf = [[] for _ in range(len(G))]
    Ef = {}
    for u in range(len(G)):
        for v in G[u]:
            Gf[v].append(u)
            Gf[u].append(v)
            Ef[(u,v)] = E[(u,v)][0]
            Ef[(v,u)] = 0
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
            
'''G = [[1,2],[2,3],[3],[]]
C = {
        (0,1):10**20,
        (0,2):10**20,
        (1,2):1,
        (1,3):10**20,
        (2,3):10**20
    }
#print(BFS(G,C,0,3))

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
print(FordFulkerson(G,C,0,5))

'''
























'''for u in G.V:
        if u!=s:
            u.color = 'w'
            u.d = float('inf')
            u.parent = None
    s.color = 'g'
    s.d = 0
    s.parent = None
    Q,i = [],0
    Q.append(s)
    
    while i<len(Q):
        u = Q[i]
        for v in G.Adj[u]:
            if v.color == 'w' and G.E[(u,v)][0] > 0:
                v.color = 'g'
                v.d = u.d + 1
                v.parent = u
                Q.append(v)
        u.color = 'b'
        i+=1
    if 
    path = []'''
        
