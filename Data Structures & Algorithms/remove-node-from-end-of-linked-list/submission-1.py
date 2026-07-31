# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        b = head
        while b:
            a.append(b) 
            b = b.next
        x = len(a) - n
        a.pop(x)
        z = ListNode(0)
        new = z
        for i in range(len(a)):
            new.next = a[i]
            new = new.next
        if new:
            new.next = None
        return z.next
