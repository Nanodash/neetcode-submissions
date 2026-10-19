# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        visited = [] # seen nodes
        node = head
        while node:
            if node in visited:
                return True
            visited.append(node)
            node = node.next
        return False
        