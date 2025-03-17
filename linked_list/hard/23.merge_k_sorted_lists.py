from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda a,b: a.val < b.val)
        pq = [head for head in lists if head]
        heapq.heapify(pq)
        dummy = curr = ListNode()
        while pq:
            node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, node.next)
            curr.next = node
            curr = curr.next
        return dummy.next
