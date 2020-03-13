def find_layered_graph(Gf,Cf,s,t):
    distance = [float('inf')]*len(Gf)
    Lf = [[] for j in range(len(Gf))]
    distance[s] = 0
    Q = [s]
    i = 0
    while i < len(Q):
        u = Q[i]
        if distance[u] >= distance[t]:
            return Lf
        for v in Gf[u]:
            if Cf[(u,v)] > 0:
                if distance[v] == distance[u] + 1:
                    Lf[u].append(v)
                elif distance[v] == float('inf'):
                    Lf[u].append(v)
                    distance[v] = distance[u] + 1
                    Q.append(v)
        i += 1
    return Lf

def find_s_t_path(Lf,Cf,s,t,seen):
    if s == t:
        return [t]
    seen[s] = True
    for v in Lf[s]:
        if not seen[v] and Cf[(s,v)] > 0:
            s_t_path = find_s_t_path(Lf,Cf,v,t,seen)
            if len(s_t_path) > 0:
                s_t_path.append(s)
                return s_t_path
    return []
     
def find_min_cap_edge(Cf,path):
    min_cap = float('inf')
    for i in range(1,len(path)):
        min_cap = min(min_cap, Cf[(path[i-1],path[i])])
    return min_cap

def augment(Cf,path):
    min_cap =  find_min_cap_edge(Cf,path)
    for i in range(1,len(path)):
        Cf[(path[i-1],path[i])] -= min_cap
        Cf[(path[i],path[i-1])] += min_cap

def prepare_residual_graph(G,U):
    Gf = [ [] for j in range(len(G))]
    Uf = {}
    for u in range(len(G)):
        for v in G[u]:
            Gf[u].append(v)
            Gf[v].append(u)
            Uf[(u,v)] = U[(u,v)]
            Uf[(v,u)] = 0
    return Gf,Uf
    

def dinic_maxflow(G,U,s,t):
    Gf,Uf = prepare_residual_graph(G,U)
    while len(find_s_t_path(Gf,Uf,s,t,[False]*len(Gf))) > 0:
        Lf = find_layered_graph(Gf,Uf,s,t)
        while True:
            path = find_s_t_path(Lf,Uf,s,t,[False]*len(Lf))
            if len(path) == 0:
                break
            path.reverse()
            augment(Uf,path)
    maxflow = 0
    for v in G[s]:
        maxflow += Uf[(v,s)]
    return maxflow
  
U = {
        (0,1) : 5,
        (1,2) : 3
    }
G = [[1],[2],[]]

G = [[1,2],[3],[1,4],[2,5],[3,5],[]]
U = {
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

#print(dinic_maxflow(G,U,0,5))
