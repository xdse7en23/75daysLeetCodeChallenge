class Solution {
public:
    string decodeString(string s) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        stack<int> numStack;
        stack<string> strStack;
        string currentStr = "";
        int k = 0;

        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                numStack.push(k);
                strStack.push(currentStr);
                k = 0;
                currentStr = "";
            } else if (c == ']') {
                int repeatCount = numStack.top();
                numStack.pop();
                string prevStr = strStack.top();
                strStack.pop();
                string temp = "";
                temp.reserve(repeatCount * currentStr.length());
                while (repeatCount--) {
                    temp += currentStr;
                }
                currentStr = prevStr + temp;
            } else {
                currentStr += c;
            }
        }

        return currentStr;
    }
};
