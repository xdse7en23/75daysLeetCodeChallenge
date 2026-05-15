# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
            
        curr = head
        nxt = curr.next
        
        while nxt:
            if curr.val == nxt.val:
                curr.next = nxt = nxt.next
            else:
                curr = nxt
                nxt = nxt.next
                
        return head
