
// Link - https://leetcode.com/problems/fibonacci-number/

// Spaace: O(1)
// Time: O(n)

class Solution {
    public int fib(int n) {
        
        if (n < 2) return n;
        
        int[] dp = {0, 1};
        int temp;
        
        for(int i=2; i < n; i++){
            
            temp = dp[1];
            dp[1] += dp[0];
            dp[0] = temp;
            
        }
        
        return dp[0] + dp[1];
        
    }
}