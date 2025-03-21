# Binary Search Tree

## properties
- organizing and storing data in a sorted manner.
- every node has at **most** two children
- left child < parent node < right child

### Insertion
new node to insert: ```key```\
currNode for comparsion: ```root```
1. initilize the current node with the root node
2. compare the **key** wiht the current
3. move **left** if the key is less than or equal to the current node value
4. move **right** if the key is greater than current node value
5. repeat steps 2 and 3 until a leaf node is reached
6. attach the **new key** as a left or right child based on the comparsion wiht the leaf node's value

implementation:
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root
```

> if there is not a node at the **parent node**'s left or right ```(node == none)```\
  we create a new node and **return** that node\
  as the recursion unwinds, we will go back to the previous step where it connects the\
  parent node with the new node we just created: ```root.left = insert(root.left, key)```\
  which gives us a new connection.
