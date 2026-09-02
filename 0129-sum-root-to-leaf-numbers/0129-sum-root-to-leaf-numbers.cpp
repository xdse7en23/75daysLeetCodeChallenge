/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int calculateSum(TreeNode* node, int currentSum) {
        if (!node) return 0;

        currentSum = currentSum * 10 + node->val;

        if (!node->left && !node->right) {
            return currentSum;
        }
        return calculateSum(node->left, currentSum) + calculateSum(node->right, currentSum);
    }

public:
    int sumNumbers(TreeNode* root) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        return calculateSum(root, 0);
    }
};
