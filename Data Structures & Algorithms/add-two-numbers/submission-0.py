# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = l1
        while b:
            a += str(b.val)
            b = b.next
        a = a[::-1]
        c = ""
        d = l2
        while d:
            c += str(d.val)
            d = d.next
        c = c[::-1]
        e = str(int(a) + int(c))
        e = e[::-1]

        z = ListNode(0)
        new = z
        for i in range(len(e)):
            new.next = ListNode(int(e[i]))
            new = new.next
        if new:
            new.next = None
        return z.next