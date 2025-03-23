# Binary Tree

## Properties
*leaf node*: nodes that do not have any child nodes
- each node in a binary tree can have at most 2 child nodes: 0, 1, 2 nodes.
- the height of a binary tree is defined as the number of edges from the root node to the deepest **leaf** node
- in a full binary tree, every node except the leaves have exactly 2 children
- in a complete binary tree, every level of the tree is completely filled except for the last level, which can be **partially filled**

## Traversal
### In-order
visits the left subtree, the node itself, then the right subtree.
### Pre-order
visits the node itself, the left subtree, and then the right subtree.
### Post-order
visits the left subtree, the right subtree, and then the node itself

## Other Trees
For **general** binary tree, the root and its children can be any value and does not follow any specific order.
But ordering rules will be applied for binary search trees, min heaps, max heap and AVL trees.

### 110 Balance Binary Tree
> solution\
 core idea: **bottom-up**. Starting from the leaf node, return the subtree depth with max-depth (from left or right) at the end of
 the recursion for every node. Before returning the value, also compare the differnce between the sum of the **left** route and the
 sum of the **right** route. Once we reach an unbalanced case, immediately return -1 and end the recursion.

### 102 Binary Tree Level Order Traversal
code: [p.102]()
```python
queue = deque([root])
```
this initializes a queue containing only the **root** node\
the brackets ```[]``` make it a list with one element, which

```python
for _ in range(len(queue)):
```
> ```len(queue)``` represents the number of nodes in the current level

essentially, we are following simple steps for the **bfs** (for more info []())
1. return ```[]``` if the current node is empty
2. initilize ```ans``` array
3. initialize a double-ended queue ```q = deque([node])``` that only contains the **root** node at the start
4. iterate through all the elements in the queue as long as it is not empty
5. make an array ```lvl=[]``` to store the node values for the **current** level
6. ```len(q)``` equals to the number of nodes in the current level. So, we run ```len(q)``` times and take 1 node out to **process** it
7. ```node = q.popleft()``` takes the node from the left of the queue (FIFO) and add its value to our ```lvl``` array
8. ```if node.left:q.append(node.left) if node.right:q.append(node.right)``` add left / right nodes to the **queue** if they exist and they will be **processed** in the next iteration
9. append ```lvl``` array into **ans** array
10. return ```ans```

### 199 Binary Tree Right Side View

#### DFS approach
This approach will be simply traverse through the binary tree from **right to left**.
1. pass an array ```ans``` which is empty as the returing value from the recursion
2. if the current node is null, we reached a child - ```None``` of a leaf node so return and cut off recirsopm
3. ```len(ans)``` stands for the number of levels of the tree we have recorded and processed, ```depth``` means the current recursion level (starting from 0)
4. ```if len(ans) == depth``` means that if the ans array's length is the same as depth, that means we have not recorded the node for the current level yet
5. so, append the current node
6. recursive iteration --> right first, left second

*note* purpose of ```depth```:
> depth means how deep the current recursion is (the no. of levels the current node is sitting on in the tree) and it is the **core** of the DFS approach

2 main uses for depth:

controls when ```ans``` adds a new node (only 1 node per level)

makes sure that the right side is always accessed first and recorded first

essentially, we skip the processing part for left nodes whenever we see a right node and make depth+=1, pass the
right node into dfs recursion again. This mechanic will cause our approach to make sure the right
side of the tree is always processed first because the left side will only start processing when
the right side reaches the end.

Also since the len(ans) has to match with depth value. So, say the recursion is finished for the right side
and the left side is called, the nodes from the start all the way to len(ans) == depth will be ignored and that is what
we want. (1 node per level and it must be the rightmost node)
#### BFS approach
