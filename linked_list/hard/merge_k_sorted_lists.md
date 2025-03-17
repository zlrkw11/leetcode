# Problem 23
## Merge k Sorted Lists
[Go to code](linked_list\hard\23.merge_k_sorted_lists.py)
[Go to my website]()
code:
```
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
```
1. make a list: pq, stores all head nodes of all non-empty linked lists
2. turn pq into a heap, the minimum value will be placed at the top
3. create a dummy node as the answer linked list, curr node to create the linked list
4. while pq is not empty, pop the top of the heap (min value)
5. if that popped node is connected to a node: push that node into the heap, making sure the next node is involved with the heap
6. connect the popped node to curr, move curr forward
7. return the dummy.next chain
