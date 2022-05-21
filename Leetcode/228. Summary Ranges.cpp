
/**
    Link - https://leetcode.com/problems/summary-ranges/
    Space: O(n)
    Time: O(n)
*/

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        
        vector<string> soln;
        
        if (nums.size() == 0) return soln;
        
        int i = 0;
        for (int j = 0; j <= nums.size(); j++){
            if (j == nums.size() || (j >=1 and nums[j-1] + 1 < nums[j])){
                if (i == j - 1){
                    soln.push_back(to_string(nums[i]));
                } else {
                    soln.push_back(to_string(nums[i]) + "->" + to_string(nums[j-1]));
                }
                i = j;
            }
        }
        
        return soln;
    }
};