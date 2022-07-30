/**
 * https://leetcode.com/problems/find-and-replace-pattern/
 * Time: O(NM)
 * Space: O(NM)
 */

class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        
        vector<string> res;
        
        for (string word: words){
            
            bool ok = true;
            vector<int> mp1(26, -1), mp2(26, -1);
            
            for (int i = 0; i < word.size() && ok; ++i){
                int j = word[i] - 'a', k = pattern[i] - 'a';
                if (mp1[j] != -1 || mp2[k] != -1){
                    ok = mp1[j] == k && mp2[k] == j;
                } else{
                    mp1[j] = k, mp2[k] = j;
                }
            }
            
            if (ok)
                res.push_back(word);
        }
        
        return res;
    }
};