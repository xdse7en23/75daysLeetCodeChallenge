#include <vector>    
#include <queue>    
#include <algorithm> 
using namespace std; 

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result; 
        if (root == nullptr) {
            return result; 
        }
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<int> currentLevel;
            for (int i = 0; i < size; i++) {
                TreeNode* curr = q.front();
                q.pop();
                currentLevel.push_back(curr->val);
                if (curr->left != nullptr) {
                    q.push(curr->left);
                }
                if (curr->right != nullptr) {
                    q.push(curr->right);
                }
            }
            result.push_back(currentLevel);
        }
        reverse(result.begin(), result.end());
        return result; 
    }
};
