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

Complexity Analysis:
--------------------

#####Adding elements

Adding elements is done in the same fashion as adding an element to
any other search tree. Start by traversing the tree starting at the
root, and move to the left or right depending on whether the point
is to be submitted on the splitting plane. 