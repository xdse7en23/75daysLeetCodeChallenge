class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        unordered_map<int, int> nextGreater;
        stack<int> s;

        for (int num : nums2) {
            while (!s.empty() && s.top() < num) {
                nextGreater[s.top()] = num;
                s.pop();
            }
            s.push(num);
        }

        vector<int> ans;
        for (int num : nums1) {
            if (nextGreater.count(num)) {
                ans.push_back(nextGreater[num]);
            } else {
                ans.push_back(-1);
            }
        }

        return ans;
    }
};
