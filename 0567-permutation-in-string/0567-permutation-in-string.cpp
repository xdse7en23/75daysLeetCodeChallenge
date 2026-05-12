class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;

        int count[26] = {0};
        for (char c : s1) count[c - 'a']++;

        int left = 0, right = 0, required = n1;

        while (right < n2) {
            if (count[s2[right] - 'a'] > 0) {
                required--;
            }
            count[s2[right] - 'a']--;
            right++;
            if (required == 0) return true;
            if (right - left == n1) {
                if (count[s2[left] - 'a'] >= 0) {
                    required++;
                }
                count[s2[left] - 'a']++;
                left++;
            }
        }

        return false;
    }
};
