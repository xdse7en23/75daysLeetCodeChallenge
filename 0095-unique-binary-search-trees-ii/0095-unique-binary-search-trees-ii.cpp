#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
private:
    unordered_map<string, vector<TreeNode*>> memo;

    vector<TreeNode*> solveUniqueBST(int start, int end) {
        vector<TreeNode*> result;
        
        if (start > end) {
            result.push_back(nullptr);
            return result;
        }
        
        string key = to_string(start) + "-" + to_string(end);
        if (memo.count(key)) {
            return memo[key];
        }
        
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> leftSubtrees = solveUniqueBST(start, i - 1);
            vector<TreeNode*> rightSubtrees = solveUniqueBST(i + 1, end);
            
            for (TreeNode* left : leftSubtrees) {
                for (TreeNode* right : rightSubtrees) {
                    TreeNode* root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    result.push_back(root);
                }
            }
        }
        
        return memo[key] = result;
    }

public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return solveUniqueBST(1, n);
    }
};
