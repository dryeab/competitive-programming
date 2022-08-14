class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        
        int max_or = 0, n = nums.size(), res = 0;
        for (int num: nums)
            max_or |= num;
        
        for (int mask = 0; mask < (1 << n); ++mask){
            int cur = 0;
            for (int i = 0; i < n; ++i){
                if ((mask >> i) & 1)
                  cur |= nums[i];
            }
            
            res += (cur == max_or);
        }
        
        return res;
    }
};