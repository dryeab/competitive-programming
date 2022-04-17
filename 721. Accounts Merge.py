
# Link - https://leetcode.com/problems/accounts-merge/

# Space: 
# Time: 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {i: i for i in range(len(accounts))}
        size = {i: 1 for i in range(len(accounts))}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2 = find(v1), find(v2)
            
            if root1 != root2:
                
                if size[root1] < size[root2]:
                    parent[root1] = root2
                    size[root2] += size[root1]
                else:
                    parent[root2] = root1
                    size[root1] += size[root2]
        
        owner = {} 
        # key: email, 
        # value: the first user who used the email
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in owner and accounts[i][0] == accounts[owner[account[j]]][0]:
                    union(i, owner[account[j]])
                owner[account[j]] = i
        
        for i in range(len(accounts)): # to be safe
            find(i)
        
        answer = defaultdict(set)
        for c, p in parent.items():
            answer[p].update(set(accounts[c][1:]))
            
        return [[accounts[key][0]] + sorted(list(value)) for key, value in answer.items()]