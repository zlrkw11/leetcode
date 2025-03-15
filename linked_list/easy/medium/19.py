from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        fast = head
        slow = head
        count = 0

        while count < n:
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        return 0