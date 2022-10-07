# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head
        while True:
            if node in visited:
                return True
            if not node:
                return False
            visited.add(node)
            node = node.next
            