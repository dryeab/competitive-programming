# link - https://leetcode.com/problems/longest-common-prefix/

# space: O(n)
# time: O(m*n) : m - average length of the strings

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_so_far = strs[0]
        
        for i in range(1, len(strs)):
            m = min(len(common_so_far), len(strs[i]))
            while (m >= 0):
                if common_so_far[:m] == strs[i][:m]:
                    break;
                m -= 1
            common_so_far = common_so_far[:m]
        
        return common_so_far
