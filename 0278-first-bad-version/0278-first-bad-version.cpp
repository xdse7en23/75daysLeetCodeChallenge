

class Solution {
public:
    int firstBadVersion(int n) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int left = 1;
        int right = n;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};
