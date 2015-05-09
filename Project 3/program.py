import Node

Info = [[]]
f = open('C:\Users\Mejia_000\Documents\Angels work\Spring 2015\COMP 401\Decision tree\Voting.csv')
for line in f:
	line = line.strip("\r\n")
	Info.append(line.split(','))
Info.remove([])
tree = {'handicapped-infants': {'y': {'water-project-cost-sharing': {'y': {'adoption-of-the-budget-resolution': {'y': {'physician-fee-freeze': {'y': {'el-salvador-aid': {'y': {'religious-groups-in-schools': {'y': {'anti-satellite-test-ban': {'y': 'republican', 'n': 'democrat'}}, 'n': 'republican'}}, 'n': 'republican'}}, 'n': 'democrat'}}, 'n': {'physician-fee-freeze': {'y': {'el-salvador-aid': {'y': 'republican', 'n': 'democrat'}}, 'n': 'democrat'}}}}, 'n': {'adoption-of-the-budget-resolution': {'y': {'physician-fee-freeze': {'y': 'republican', 'n': 'democrat'}}, 'n': {'physician-fee-freeze': {'y': 'republican', 'n': {'el-salvador-aid': {'y': 'democrat', 'n': {'religious-groups-in-schools': {'y': 'democrat', 'n': {'anti-satellite-test-ban': {'y': {'aid-to-nicaraguan-contras': {'y': {'mx-missile': {'y': {'immigration': {'y': {'synfuels-corporation-cutback': {'n': {'education-spending': {'n': {'superfund-right-to-sue': {'n': {'crime': {'y': 'republican', 'n': 'democrat'}}}}}}}}}}}}}}}}}}}}}}}}}}, 'n': {'water-project-cost-sharing': {'y': {'adoption-of-the-budget-resolution': {'y': {'physician-fee-freeze': {'y': {'el-salvador-aid': {'y': {'religious-groups-in-schools': {'y': {'anti-satellite-test-ban': {'y': 'republican', 'n': {'aid-to-nicaraguan-contras': {'y': 'democrat', 'n': {'mx-missile': {'n': {'immigration': {'y': {'synfuels-corporation-cutback': {'y': 'democrat', 'n': 'republican'}}}}}}}}}}}}}}, 'n': 'democrat'}}, 'n': {'physician-fee-freeze': {'y': {'el-salvador-aid': {'y': {'religious-groups-in-schools': {'y': {'anti-satellite-test-ban': {'y': 'republican', 'n': {'aid-to-nicaraguan-contras': {'n': {'mx-missile': {'y': 'republican', 'n': {'immigration': {'y': 'republican', 'n': {'synfuels-corporation-cutback': {'y': {'education-spending': {'y': {'superfund-right-to-sue': {'y': 'republican', 'n': 'democrat'}}}}, 'n': 'republican'}}}}}}}}}}}}}}, 'n': 'democrat'}}}}, 'n': {'adoption-of-the-budget-resolution': {'y': {'physician-fee-freeze': {'y': 'republican', 'n': 'democrat'}}, 'n': {'physician-fee-freeze': {'y': {'el-salvador-aid': {'y': {'religious-groups-in-schools': {'y': {'anti-satellite-test-ban': {'y': 'republican', 'n': {'aid-to-nicaraguan-contras': {'n': {'mx-missile': {'n': {'immigration': {'y': 'republican', 'n': {'synfuels-corporation-cutback': {'y': {'education-spending': {'y': {'superfund-right-to-sue': {'y': {'crime': {'y': {'duty-free-exports': {'n': {'export-administration-act-south-africa': {'y': 'republican', 'n': 'democrat'}}}}}}}}}}, 'n': 'republican'}}}}}}}}}}, 'n': 'republican'}}, 'n': 'republican'}}, 'n': 'democrat'}}}}}}}}
attributes = ['handicapped-infants', 'water-project-cost-sharing', 'adoption-of-the-budget-resolution', 'physician-fee-freeze', 'el-salvador-aid', 'religious-groups-in-schools', 'anti-satellite-test-ban', 'aid-to-nicaraguan-contras', 'mx-missile', 'immigration', 'synfuels-corporation-cutback', 'education-spending', 'superfund-right-to-sue', 'crime', 'duty-free-exports', 'export-administration-act-south-africa', 'class']
count = 0
for entry in Info:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.Value)
		Value = entry[index]
		if(Value in tempDict.keys()):
			child = Node.Node(Value, tempDict[Value])
			result = tempDict[Value]
			tempDict = tempDict[Value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	print ("entry%s = %s" % (count, result))
