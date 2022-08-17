# https://leetcode.com/problems/count-nodes-with-the-highest-score/
# Time: O(N)
# Space: O(N)

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        n = len(parents)
        tree = [[] for _ in range(n)]
        children = [0 for _ in range(n)]

        for i in range(1, n):
            tree[parents[i]].append(i)

        def countChildren(node):

            children[node] = 1
            for child in tree[node]:
                children[node] += countChildren(child)

            return children[node]

        mx, cnt, total = 0, 0, countChildren(0)

        def dfs(node):
            nonlocal total, mx, cnt

            left, prod = total - 1, 1

            for child in tree[node]:
                prod *= children[child] or 1
                left -= children[child]
                dfs(child)

            prod *= left or 1

            if prod > mx:
                mx, cnt = prod, 1
            elif prod == mx:
                cnt += 1

        dfs(0)

        return cnt
