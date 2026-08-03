# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
        a.sort()
        dummy = ListNode(0)
        curr = dummy

        for n in a:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next