
// Link - https://leetcode.com/problems/binary-tree-paths/

class Solution {
public:
    
    vector<string> soln;
    
    vector<string> binaryTreePaths(TreeNode* root) {
        
        helper(root, ""); return soln;
    }
    
    void helper(TreeNode* root, string path){
        
        path += (path == "" ? "" : "->") + to_string(root->val);
        
        if (root->left == nullptr && root->right == nullptr){
            soln.push_back(path);
            return;
        }
        
        if (root->left) helper(root->left, path);
        if (root->right) helper(root->right, path);
        
    }
};