/*
    https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
    Time: O(n)
    Space: O(1)
*/

class Solution {
public:
    int minDeletions(string s) {
        
        int count[26] = {};
        
        for (char x: s)
            count[x-'a']++;
        
        int ans = 0;
        unordered_set<int> used;
        
        for (int freq: count){
            while (freq && used.count(freq)){
                freq--;
                ans++;
            }
            used.insert(freq);
        }
        
        return ans;
    }
};