# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return None
        
        # Here we are detecting if there is a cycle using Floyd's Tortoise and Hare
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # A meeting point indicates a cycle exists
                break
        else:
            # If we exit the loop normally (no break), there's no cycle
            return None
        
        # Here we are finding the node where the cycle begins
        # Move one pointer to head, keep the other at meeting point
        # Advance both one step at a time; they will meet at the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
