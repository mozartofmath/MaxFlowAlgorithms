def Extract_Max(Queue,largest):
    maximum = -float('inf')
    max_element = None
    for v in Queue:
        if largest[v] >= maximum:
            maximum = largest[v]
            max_element = v
    Queue.remove(max_element)
    
    return max_element

def MAPDijkstra(G,E,s,t):
    largest = {}
    parent = {}
    for i in range(len(G)):
        largest[i] = -float('inf')
        parent[i] = None
    largest[s] = float('inf')
    S = set()
    Q = [i for i in range(len(G))]
    while len(Q)>0:
        u = Extract_Max(Q,largest)
        S.add(u)
        for v in G[u]:
            if largest[v]< min(largest[u],E[(u,v)]):
                largest[v] = min(largest[u],E[(u,v)])
                parent[v] = u
    if parent[t] == None:
        return [],0
    path = []
    cur = t
    cap = float('inf')
    while parent[cur] != None:
        path.append((parent[cur],cur))
        cap = min(cap,E[(parent[cur],cur)])
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
        path,cap = MAPDijkstra(Gf,Ef,s,t)
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
#print(FordFulkerson(G,C,0,3))
