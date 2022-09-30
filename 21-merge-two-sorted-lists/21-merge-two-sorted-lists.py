# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        res = None
        if not p1 and not p2:
            return p1
        if not p1:
            return p2
        if not p2:
            return p1

        if list1.val > list2.val:
            res = p2
            p2 = p2.next
        else:
            res = p1
            p1 = p1.next
        d = res
        while p1 or p2:
            if not p1:
                res.next = p2
                p2 = p2.next
                res = res.next
                continue
            if not p2:
                res.next = p1
                p1 = p1.next
                res = res.next
                continue
            if p1.val > p2.val:
                res.next = p2
                p2 = p2.next
            else:
                res.next = p1
                p1 = p1.next
            res = res.next
        print(d)
        return d