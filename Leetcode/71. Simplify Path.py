class Solution:
    def simplifyPath(self, path: str) -> str:
        
        res = []
        for p in path.split('/'):
            if p == '..':
                if res: res.pop()
            elif p and p != '.':
                res.append(p)
        
        return '/' + '/'.join(res)