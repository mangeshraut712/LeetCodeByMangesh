import sys
sys.setrecursionlimit(10**7)

class Solution:
    def criticalConnections(self, n, connections):
        g=[[] for _ in range(n)]
        for u,v in connections:
            g[u].append(v); g[v].append(u)
        disc=[0]*n; low=[0]*n; t=1; res=[]
        def dfs(u,p):
            nonlocal t
            disc[u]=low[u]=t; t+=1
            for v in g[u]:
                if v==p: continue
                if not disc[v]:
                    dfs(v,u)
                    low[u]=min(low[u],low[v])
                    if low[v]>disc[u]: res.append([u,v])
                else:
                    low[u]=min(low[u],disc[v])
        dfs(0,-1)
        return res
