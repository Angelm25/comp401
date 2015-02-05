#include <iostream>
#include <vector>

using namespace std;
/*
This file will define the different set of points that will be used in the Kd-tree.
The kd-tree will be a 2D tree, and will be used a sort of flat graph
*/

struct point // This will define the points that we work with
{
	double a, b;

	point () : a(0.), b(0.)
	{}
	point(double x, double y) : a(x), b(y)
	{} 
};


struct kd_tree::node // The node structure that will hold the information for the kd-tree
{
	size_t i0, i1, split; // i0 and i1 will note the indexes of the child nodes

	node(): i0(-1), i1(-1), split(-1) // the split point index. split(-1) will refer to a leaf node
	{} 
	friend bool is_leaf(const node &n)
	{ return n.split==size_t(-1);}
};

//stack for stack based implementation
//
struct build_task
{
	size_t first, last, node, dim; // First, last will denote the point range 
	// node is index of current node, dim is current dimension to split in
};

inline void expand(point &min, point &max, const point &p)
//expanding the bounding box points for subsequently added points
{
	if (p.x<min.x) 
		min.x = p.x;
	else if (p.x>max.x) 
		max.x = p.x;
	if (p.y<mix.y) 
		min.y = p.y;
	else if (p.y>max.y) 
		max.y = p.y;
	return;
}

struct lower_x
{
	const std::vector<point> &points;

	lower_x(const std:vector<points> &p) : points(p)
	{}
	
}

/*-----------------------------------------------------------------*/
// Seperation for Kd-tree class 
/*-----------------------------------------------------------------*/

using std::vector;

struct kd_tree;
{
	struct node; 

	point min, max; // will store lower and upper points of the bounding rectangle
	vector<node> nodes;

	kd_tree(const vector<point> &points);
};