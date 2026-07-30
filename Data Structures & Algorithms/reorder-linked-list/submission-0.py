# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 0
        n = []
        b = head
        while b:
            n.append(b) 
            b = b.next
        b = head
        for i in range(len(n) // 2):
            last = n.pop()
            nextt = b.next
            b.next = last
            last.next = nextt
            b = nextt
        b.next = None
        