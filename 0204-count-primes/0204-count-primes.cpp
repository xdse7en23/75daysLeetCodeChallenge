#include <iostream>
#include <cstring>

using namespace std;
static const int fast_io = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;
        bool* isPrime = new bool[n];
        memset(isPrime, true, n);

        int count = 1;
        for (int i = 3; i * i < n; i += 2) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += 2 * i) {
                    isPrime[j] = false;
                }
            }
        }
        for (int i = 3; i < n; i += 2) {
            if (isPrime[i]) {
                count++;
            }
        }
        delete[] isPrime;

        return count;
    }
};
