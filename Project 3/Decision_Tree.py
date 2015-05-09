#Angel Mejia
#March 28, 2015
#Decision Tree

import math

#catch entry in a list
def catch(entry, list):
    
    for i in list:
    
        if entry(i): 
            return True
    
        else:
            return False

#find most common value for Attribute
def MostCom(Attribute, data, destination):
    
    #destination attribute
    ValueFrq = {}
    
    #find destination in data
    index = Attribute.index(destination)
    
    #calculate freq of values in destination attr
    for tuple in data:
    
        if (ValueFrq.has_key(tuple[index])):
            ValueFrq[tuple[index]] += 1 
    
        else:
            ValueFrq[tuple[index]] = 1
    
    max = 0
    mostcommon = ""
    
    for key in ValueFrq.keys():
        
        if ValueFrq[key]>max:
            max = ValueFrq[key]
            mostcommon = key
    
    return mostcommon

#Calculates the entropy of the given data set for the destination attr
def entropy(Attribute, data, AttributeDest):

    ValueFrq = {}
    dataEntropy = 0.0
    
    #find index of the destination attribute
    i = 0
    for entry in Attribute:
    
        if (AttributeDest == entry):
            break
        ++i
    
    # Calculate the frequency of each of the values in the destination attr
    for entry in data:
    
        if (ValueFrq.has_key(entry[i])):
            ValueFrq[entry[i]] += 1.0
    
        else:
            ValueFrq[entry[i]]  = 1.0

    # Calculate the entropy of the data for the destination attr
    for freq in ValueFrq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return dataEntropy

def gain(Attribute, data, attr, AttributeDest):

    #calculates information gain from splitting data in attr
    ValueFrq = {}
    subsetEntropy = 0.0
    
    #find index of the attribute
    i = Attribute.index(attr)

    # Calculate the freq of vals in the destination 
    for entry in data:
        
        if (ValueFrq.has_key(entry[i])):
            ValueFrq[entry[i]] += 1.0
        
        else:
            ValueFrq[entry[i]]  = 1.0
   
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
    for val in ValueFrq.keys():
        
        valProb        = ValueFrq[val] / sum(ValueFrq.values())
        dataSubset     = [entry for entry in data if entry[i] == val]
        subsetEntropy += valProb * entropy(Attribute, dataSubset, AttributeDest)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the destination attribute (and return it)
    return (entropy(Attribute, data, AttributeDest) - subsetEntropy)

#choose best attibute 
def chooseAttr(data, Attribute, destination):

    best = Attribute[0]
    maxGain = 0;
    
    for attr in Attribute:
    
        newGain = gain(Attribute, data, attr, destination) 
        
        if newGain>maxGain:
            maxGain = newGain
            best = attr

    return best

#get values in the column of the given attribute 
def getValues(data, Attribute, attr):

    index = Attribute.index(attr)
    values = []
    
    for entry in data:
    
        if entry[index] not in values:
            values.append(entry[index])
    return values

def getExamples(data, Attribute, best, val):
    
    examples = [[]]
    index = Attribute.index(best)
    
    for entry in data:
        #find entries with the give value
    
        if (entry[index] == val):
            newEntry = []
            #add value if it is not in best column
    
            for i in range(0,len(entry)):
    
                if(i != index):
                    newEntry.append(entry[i])
            examples.append(newEntry)
    
    examples.remove([])
    return examples

def makeTree(data, Attribute, destination, recursion):

    recursion += 1
    #Returns a new decision tree based on the examples given.
    
    data = data[:]
    vals = [record[Attribute.index(destination)] for record in data]
    default = MostCom(Attribute, data, destination)

    # If the dataset is empty or the Attribute list is empty, return the
    # default value. When checking the Attribute list for emptiness, we
    # need to subtract 1 to account for the destination attribute.
    
    if not data or (len(Attribute) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    
    else:
        # Choose the next best attribute to best classify our data
        best = chooseAttr(data, Attribute, destination)

        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}
    
        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        
        for val in getValues(data, Attribute, best):
            # Create a subtree for the current value under the "best" field
        
            examples = getExamples(data, Attribute, best, val)
            newAttr = Attribute[:]
            newAttr.remove(best)
            subtree = makeTree(examples, newAttr, destination, recursion)
    
            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree
    
    return tree