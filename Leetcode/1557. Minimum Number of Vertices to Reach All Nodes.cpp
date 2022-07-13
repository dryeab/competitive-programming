/**
 * https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
 * Time: O(|E|)
 * Space: O(n)
 */

class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        
        vector<int> degree(n), res;
        for (auto edge : edges)
            degree[edge[1]]++;
        
        for (int i = 0; i < n; ++i)
            if (degree[i] == 0)
                res.push_back(i);
        
        return res;
    }
};