class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        vector<string> phone_map = {
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
        
        vector<string> result;
        string current = "";
        
        backtrack(0, digits, current, phone_map, result);
        return result;
    }

private:
    void backtrack(int index, const string& digits, string& current, const vector<string>& phone_map, vector<string>& result) {
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }
        
        string letters = phone_map[digits[index] - '0'];
        for (char letter : letters) {
            current.push_back(letter);
            backtrack(index + 1, digits, current, phone_map, result);
            current.pop_back();
        }
    }
};
