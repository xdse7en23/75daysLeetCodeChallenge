#include <vector>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        int totalElements = 1 << n;
        result.reserve(totalElements);
        
        for (int i = 0; i < totalElements; i++) {
            result.push_back(i ^ (i >> 1));
        }
        
        return result;
    }
};

