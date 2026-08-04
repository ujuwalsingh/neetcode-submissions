# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        sub = []
        while head:
            sub.append(head.val)
            if len(sub) == k:
                sub.reverse()
                arr.extend(sub)
                sub = []
            head = head.next
        if len(sub) >= 0:
            arr.extend(sub)
        
        dummy = ListNode(0)
        curr = dummy
        for n in arr:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next
