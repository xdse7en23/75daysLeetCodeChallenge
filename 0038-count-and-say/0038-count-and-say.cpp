#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        
        string result = "1";
        
        for (int i = 2; i <= n; i++) {
            string next_result = "";
            int len = result.length();
            
            for (int j = 0; j < len; j++) {
                int count = 1;
                while (j + 1 < len && result[j] == result[j + 1]) {
                    count++;
                    j++;
                }
                next_result += to_string(count) + result[j];
            }
            result = next_result;
        }
        
        return result;
    }
};

