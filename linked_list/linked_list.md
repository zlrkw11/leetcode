# Linked List

## P19 

### solution 1 - 2 pointers
by using **fast n slow** pointers, we can traverse the linked list with fast first until it went n steps. Then 
use slow and fast together, make fast go all the way to the end. At that moment, the slow pointer will be n steps away
from the end. 

### solution 2 - length function
we can solve this question by having a **getListSize(head)** function to run a while loop and get the length of the linked list.\   
Then get the index of the target value to remove by using ```length - n```.\
Then, use a while loop to iterate through the linked list from the start until i reaches the node right before the target node.\
Use curr.next = curr.next.next to skip over the target node by establishing a new link between the target-1 and target+1.
