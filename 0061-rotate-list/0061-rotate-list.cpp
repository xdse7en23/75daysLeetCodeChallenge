/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        if (!head || !head->next || k == 0) return head;
        int length = 1;
        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
            length++;
        }
        k = k % length;
        if (k == 0) return head; 
        tail->next = head;
        ListNode* new_tail = head;
        for (int i = 0; i < length - k - 1; ++i) {
            new_tail = new_tail->next;
        }
        ListNode* new_head = new_tail->next;
        new_tail->next = nullptr;

        return new_head;
    }
};
