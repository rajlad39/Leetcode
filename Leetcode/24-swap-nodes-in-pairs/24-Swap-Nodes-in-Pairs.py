# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next

            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second

            # Re-position prev for the next pair
            prev = first

        return dummy.next