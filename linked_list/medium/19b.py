from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        # calcualte length
        length = self.getListSize(head)

        # figure out index from left
        index = length - n
        if index == 0:
            return head.next

        # traverse and skip the node at index
        curr = head
        i = 0
        while i != index - 1:
            curr = curr.next
            i += 1
        curr.next = curr.next.next

        return head
    
    def getListSize(self, head):
        if head is None:
            return 0

        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        return length
