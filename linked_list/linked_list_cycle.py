class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head == None:
           return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        