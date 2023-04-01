# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        sum = ans
        carry = 0
        while l1 or l2:
            if l1 and l2:
                s = l1.val + l2.val + carry
                carry, s = divmod(s, 10)

                sum.next = ListNode(s % 10)
                sum = sum.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                carry, s = divmod(l1.val + carry, 10)
                sum.next = ListNode(s)
                sum = sum.next
                l1 = l1.next
            else:
                carry, s = divmod(l2.val + carry, 10)
                sum.next = ListNode(s)
                sum = sum.next
                l2 = l2.next

        if carry:
            sum.next = ListNode(1)
            sum = sum.next
        return ans.next