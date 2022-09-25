/**
 * https://leetcode.com/problems/maximum-product-after-k-increments/
 * Time: O(NlogN + klogN)
 * Space: O(N)
 */

class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        
        priority_queue<int, vector<int>, greater<int>> pq(nums.begin(), nums.end());
        
        while (k--){
            int num = pq.top();
            pq.pop();
            pq.push(num + 1);
        }
        
        long long MOD = 1e9 + 7, res = 1;
        while (!pq.empty()){
            (res *= (pq.top() % MOD)) %= MOD;
            pq.pop();
        }
        
        return res;
    }
};