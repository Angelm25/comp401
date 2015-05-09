Project 3: Decision Tree
===============================

###Decision Tree 

A decision tree falls under a subfield of of machine learning within artificial intelligence.
Typically used for classification purposes. Contains statements that result in classification
once applied to a record of a data set. They are ultimately made with the ability to learn.
The heuristic used in this decision tree is an ID3 heurisitic.

##ID3 heuristic

An ID3 heuristic uses the concept of entropy and disorder in a data set to reduce amount
of info needed to describe each data piece. Most uses of this heuristic is to find the best 
attribute to classify records in a data set. The idea for this also comes from information
theory. 

Entropy represents all the possiblilities in a data set, while Information gain which comes 
from information thoery is used to gain information from the data sets. 

#Other information

This program runs in a O log(n) complexity. The more data you feed it the longer it will take to run
the program.

To use this program you feed it in a data set by changing the code directory in the main.py. You have 
to give it a dataset first to train it. After you have to give it another file, with different information
pertaining to that dataset, and run the program.py which is produced by the main function. Afterwards
the program should classify your data and return an output pertaining to it. 

The source i used to work through this is here:

1. http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=1 
