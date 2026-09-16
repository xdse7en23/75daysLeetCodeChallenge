#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if (n <= 1) return n;
        
        int totalCandies = 1;
        int up = 0, down = 0, peak = 0;
        
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                down = 0;
                up++;
                peak = up;
                totalCandies += 1 + up;
            } else if (ratings[i] == ratings[i - 1]) {
                up = 0;
                down = 0;
                peak = 0;
                totalCandies += 1;
            } else {
                up = 0;
                down++;
                totalCandies += 1 + down - (peak >= down ? 1 : 0);
            }
        }
        
        return totalCandies;
    }
};
