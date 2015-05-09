import Decision_Tree

def main():
    #Insert input file

    file = open('C:\Users\Mejia_000\Documents\Angels work\Spring 2015\COMP 401\Decision tree\VoteTrain.csv')
    #how the machine will learn.

    target = "class"

    Info = [[]]
    
    for line in file:
        line = line.strip("\r\n")
        Info.append(line.split(','))
    
    Info.remove([])
    attributes = Info[0]
    Info.remove(attributes)
    
    #Run ID3
    tree = Decision_Tree.makeTree(Info, attributes, target, 0)
    print "generated decision tree"
    
    #create program
    file = open('program.py', 'w')
    file.write("import Node\n\n")
    
    #open input
    file.write("Info = [[]]\n")
    
    #tests
    file.write("f = open('C:\Users\Mejia_000\Documents\Angels work\Spring 2015\COMP 401\Decision tree\Voting.csv')\n")
    
    #get Info
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tInfo.append(line.split(','))\n")
    file.write("Info.remove([])\n")
    
    #input dictionary tree
    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("for entry in Info:\n")
    file.write("\tcount += 1\n")
    
    #copy it
    file.write("\ttempDict = tree.copy()\n")
    file.write("\tresult = \"\"\n")
    
    #generate tree
    file.write("\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    
    #attribute
    file.write("\t\tindex = attributes.index(root.Value)\n")
    file.write("\t\tValue = entry[index]\n")
    
    #checks existance of key
    file.write("\t\tif(Value in tempDict.keys()):\n")
    file.write("\t\t\tchild = Node.Node(Value, tempDict[Value])\n")
    file.write("\t\t\tresult = tempDict[Value]\n")
    file.write("\t\t\ttempDict = tempDict[Value]\n")
    
    #if none, will break
    file.write("\t\telse:\n")
    file.write("\t\t\tprint \"can't process input %s\" % count\n")
    file.write("\t\t\tresult = \"?\"\n")
    file.write("\t\t\tbreak\n")
    
    #solutions 
    file.write("\tprint (\"entry%s = %s\" % (count, result))\n")
    print "written program"
    
    
if __name__ == '__main__':
    main()