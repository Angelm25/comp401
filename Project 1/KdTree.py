import sys

class Kdtree:
	"""docstring for Kdtree"""

	def __init__(self, points):


		#There needs to be 2 points
		assert len(points) > 1
		for point in points: 
			assert len(point) == 2


		NEWpoints = self.Tree_array(points)
		self.tree = self.TreeBuilding(0, NEWpoints)

	def Tree_array(self, list): 
		"""
		This function will accept a list and if the list contains
		any repeats of the elements it will create a new list without it.
		"""
		New_List = []

		for i in list:
			if i not in New_List:
				New_List.append(i)

		assert len(New_List) <= len(list) 
		return New_List

	def TreeBuilding(self, depth, points):

		if len(points) == 0:
			return ()
		elif len(points) == 1:
			assert len(points[0]) == 2
			return points[0]

		assert len(points) > 1

		#Will use the depth of tree to partition on x or y
		#It will decide on how to partition if depth is Even or odd
		#If even will partition on X, and y if it is odd.
		if (depth % 2 == 0):
			median, pointsTuple = self.partX(points)
		else:
			median, pointsTuple = self.partY(points)

		leftPoints, rightPoints = pointsTuple

		#will return value that represents node

		leftChildren = self.TreeBuilding(depth + 1, leftPoints)
		rightChildren = self.TreeBuilding(depth + 1, rightPoints)
		return (median, leftChildren, rightChildren)

	def partX(self, points):

		assert len(points) > 0

		points.sort(self.__cmp_by_x)
		medianPoint = len(points)/2
		splitValue = points[medianPoint][0]
		#
		if splitValue == points[0][0]:
			splitValue = splitValue + 1

		pointsLT, pointsGT = self.__split(splitValue, points, 0)

		return (splitValue, (pointsLT,pointsGT))

	def partY(self, points):
		#
		assert len(points) > 0

		points.sort(self.__cmp_by_y)
		medianPoint = len(points)/2
		splitValue = points[medianPoint][1]

		#
		if splitValue == points[0][1]:
			splitValue = splitValue + 1

		pointsLT, pointsGT = self.__split(splitValue, points, 1)

		return (splitValue, (pointsLT, pointsGT))

	def __split(self, value, sortedpoints, index):
		#Split points into two sets based on value

		if len(sortedpoints) == 0:
			return [[],[]]

		head = sortedpoints[0]
		tail = sortedpoints[1:]

		if (head[index] < value):
			lt, gt = self.__split(value, tail, index)
			retval = [[head] + lt, gt]
		else:
			retval = [[], sortedpoints]
		return retval


	def __cmp_by_x(self, point1, point2):


		assert len(point1) == 2
		assert len(point2) == 2

		x1 = point1[0]
		x2 = point2[0]

		if x1 > x2:
			retval = 1
		elif x1 == x2:
			retval = 0
		else:
			retval = -1

		assert retval in (1, 0, -1)
		return retval

	def __cmp_by_y(self, point1, point2):


		assert len(point1) == 2
		assert len(point2) == 2

		y1 = point1[1]
		y2 = point2[1]

		if y1 > y2:
			retval = 1
		elif y1 == y2:
			retval = 0
		else:
			retval = -1

		assert retval in (1, 0, -1)
		return retval

	def NearestNeighbor(self, point):

		assert len(point) == 2
		assert len(self.tree) == 3

		xVal, yVal = point
		nearest = self.NearNeighborSearch(self.tree, xVal, yVal)

		assert len(nearest) == 2
		return nearest

	def NearNeighborSearch(self, tree, LeftVal, RightVal):

		if len(tree) < 3:
			return tree

		assert len(tree) == 3

		MedValue = tree[0]

		if LeftVal < MedValue:
			subtree = tree[1]
		else:
			assert LeftVal >= MedValue
			subtree = tree[2]

		"""Left and right values are switched each time the
		   Recursion takes place. Discards need to record depth
		   to do a comparison."""

		retval = self.NearNeighborSearch(subtree, RightVal, LeftVal)


		if len(retval) == 0:
			subtree = tree[2]
		elif len(tree[2]) == 0:
			subtree = tree[1]
		retval = self.NearNeighborSearch(subtree, RightVal, LeftVal)

		assert len(retval) == 2
		return retval

if __name__ == '__main__':
	import random
	from ast import literal_eval

	MaxPoints = 1200000
	Xmax = 1280
	Ymax = 1024

	r = random.Random()
	dataset = open('C:data set3.txt', 'r')

	points = []

	for i in dataset:
		to_tup = literal_eval(i)
		points.append(to_tup)

	#points = [(6, 1), (5, 5), (9, 6), (3, 6), (4, 9), (4, 0), (7, 9), (2, 9)]
	#print "Building tree for points\n\t%s\n" % points	
	
	print "Building the Tree."

	tree = Kdtree(points)
	print 'Done\n'


	SrchPt = (r.randint(0, Xmax), r.randint(0, Ymax))
	
	#SrchPt = (5, 4)
	
	print "Nearest neighbour to %s in the the tree is: " %(SrchPt,)

	NearestPt = tree.NearestNeighbor(SrchPt)
	print '%s\n' % (NearestPt,)

	NumTimes = 1000000
	stmt = 'tree.NearestNeighbor(%s)' % (SrchPt,)
	setup = 'from __main__ import Kdtree; tree = Kdtree(%s)' % points
	#print "Timing search... "
	#timer = timeit.Timer(stmt, setup)
	#sec = timer.timeit(NumTimes)

	#print "done (%fs/search)\n" % (sec/NumTimes,)







		
