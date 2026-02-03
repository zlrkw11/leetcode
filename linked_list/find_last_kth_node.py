from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def LastKth(self, head: Optional[ListNode], k:int) -> Optional[ListNode]:
        j = head
        i = head
        for _ in range(k):
            if not j: return None
            j = j.next
        
        while j:
            j = j.next
            i = i.next

        return i