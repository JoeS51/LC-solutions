class Solution:
    def candy(self, ratings: List[int]) -> int:
        adj = defaultdict(list)
        ined=[0]*len(ratings)
        for i in range(1, len(ratings)):
            prev = ratings[i-1]
            curr=ratings[i]
            if curr>prev:
                adj[i-1].append(i)
                ined[i]+=1
            elif prev > curr:
                adj[i].append(i-1)
                ined[i-1]+=1
        q = []
        for i in range(len(ined)):
            if ined[i] == 0:
                q.append(i)

        res =[0] * len(ratings)
        print(ined)
        print(adj)
        num=0
        while q:
            
            currlen=len(q)
            print(q)
            num+=1
            for idx in range(currlen):
                
                curr= q.pop(0)
                res[curr] = num
                if curr in adj:
                    for n in adj[curr]:
                        
                    
                        ined[n]-=1
                        if ined[n]==0:
                            q.append(n)
        print(res)
        return sum(res)

            
            
            
            
            
        
        
            
        
        

