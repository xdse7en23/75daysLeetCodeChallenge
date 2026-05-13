class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            else {
                right = mid;
            }
        }
        return left;
    }
};
