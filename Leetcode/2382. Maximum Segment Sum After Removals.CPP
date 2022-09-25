/**
 * https://leetcode.com/problems/maximum-segment-sum-after-removals/
 * Time: O(NlogN)
 * Space: O(N)
 */

typedef long long ll;

class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        
        ll n = nums.size(), cur = 0;
        vector<ll> parent(n), sz(n), sum(n);
        
        for (ll i = 0; i < n; ++i)
            parent[i] = i, sz[i] = 1;
        
        function<ll(ll)> find;
        find = [&](ll i){
            if (i == parent[i])
                return i;
            return parent[i] = find(parent[i]);
        };
        
        auto unite = [&](ll i, ll j){
            
            i = find(i), j = find(j);
            
            if (sz[i] > sz[j])
                swap(i, j);
            
            sz[j] += sz[i];
            parent[i] = j;
            
            sum[j] += sum[i];
            
            cur = max(cur, sum[j]);
        };
        
        vector<ll> res;
        for (ll i = n - 1; i >= 0; --i){
            
            res.push_back(cur);
            
            ll j = removeQueries[i];
            
            sum[j] = nums[j];
            
            cur = max(cur, sum[j]);
            
            if (j > 0 && sum[j - 1] > 0)
                unite(j - 1, j);
            
            if (j + 1 < n && sum[j + 1] > 0)
                unite(j, j + 1);
        }
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};