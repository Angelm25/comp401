KD Tree Implementation
-----------------------------
Angel Mejia
-----------------------------
A KD-tree is a data-structure with space partitioning often used for 
organizing data in a k-dimensional space. They are a special case
for binary space partitioning trees KD-tree's can be useful for searches 
involving multidimensional search keys. 

A kd tree is binary tree where every node is a k-dimensional point. They are
used for storing coordinates to make nearest neighbor searching or range
searches reletively fast. A Kd-tree has it's values always stored in leaves
and what the internal nodes represent differs on the depth of the tree. 

Documentation:
--------------

#####To use this code:

Read your list of points into the dataset and build and run the code.

Utilize nearest neighbor search by setting "PointSearch" equal to 
which ever point you wish to find the nearest neighbor for. 

#####Recursion Depth Limit:

The recursion depth limit for this python implementation is 1000.
Datasets with larger sets may bring up an issue. 

A more balanced tree, or iterative as opposed to recursive implementation
may remedy this issue. 

Complexity Analysis:
--------------------

#####Adding elements   O(log n)   (O(n) worst case)

Adding elements is done in the same fashion as adding an element to
any other search tree. Start by traversing the tree starting at the
root, and move to the left or right depending on whether the point
is to be submitted on the splitting plane. After locating node for 
the child then add new point depending on which splitting plane
contains new node.

Adding points in this manner may cause tree to become unbalanced. 

#####Nearest Neighbor Search 	O(log n) 	(O(n) worst case)

Nearest neighbor search is used to find which point in a set
is closest to another point. The search function is similar to
a search in a binary search tree but you must keep track of the
depth of the tree, to know whether to compare the x or the y value.

This implementation opts not to keep track of the current depth
in the tree while searching. Instead it compares the median with
the first of two search-coordinates and then swaps them during
recursion. This implementation allows it to search faster.

references
----------

1. [Python Style guide](https://www.python.org/dev/peps/pep-0008/)
2. [KD-trees](http://en.wikipedia.org/wiki/K-d_tree)
3. [More advnaced KD-tree implementation](http://rosettacode.org/wiki/K-d_tree)

