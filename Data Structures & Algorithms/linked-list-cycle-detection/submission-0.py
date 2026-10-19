# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        visited = [] # seen vals
        node = head
        while node:
            if node.val in visited:
                return True
            visited.append(node.val)
            node = node.next
        return False
        