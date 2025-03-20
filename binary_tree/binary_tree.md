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
