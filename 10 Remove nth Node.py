# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Using Two pointers
        #Time: O(n)
        #Space: O(1)
        t1 = t2 = head

        while (t2 != None):
            t2 = t2.next
            if (n < 0):
                t1 = t1.next
            n -= 1          
        
        if n > -1:
            head = head.next
            return head
        else:
            t1.next = t1.next.next

        return head
        
