#include <iostream>
#include <vector>

using namespace std;
using std::vector;
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



//stack for stack based implementation
//
struct build_task
{
	size_t first, last, node, dim; // First, last will denote the point range 
	// node is index of current node, dim is current dimension to split in
};





kd_tree::kd_tree(const std::vector<point> &points) 
{
	//setting up to get a vector<point> of points to build the tree
	
	const size_t
		stack_size = 32,
		count = points.size(); //initialize stack with depth of 32

	if (count==0)
		return; //if 0 points leaves tree empty 

	size_t *index = new size_t[count];
	//allocate index array and have the ith element point to the ith point
	for (size_t i = 0; i < count; ++i)
		index[i] = i; // elements in the array are going to be partitioned

	const size_t
		m = next_pow_of_2(count),
		node_count = std::min(m-1, 2*count - m/2 -1);
	nodes.reserved(node_count);

	nodes.push_back(node()); //append a node 
	building_task tasks[stack_size] = //task stack initialization
		{0, count -1, 0, 0} //first, last, node, dimension. respectively.
	//Should consider all points!!! current node is 0, dimension is also 0

	int current_task = 0; //current task counter
	point //initialization of min and max points
	min (std::numeric_limits<double>::max(), std::numeric_limits<double>::max()),
	max (-std::numeric_limits<double>::max(), std::numeric_limits<double>::max())

	do 
	{
		//gets the current task and node
		build_task task = tasks[current_task];
		node &n = nodes[task.node];

		if (task.last - task.first<=1) //if there is only 1 or 2 points, will set leaf node
		{
			n.i0 = index[task.first]; //if 1 point only fill i0
			expand(min, max, points[n.i0]); 
			if (task.first!=task.last) 
			{
				n.i1 = index[task.last]; //if 2 points fill i0 and i1
				expand(min, max, points[n.i0]); //expand min and max to reflect the bounding rectangle
			}
			assert(is_leaf(n));
			--current_task; //Decrement current tast counter
			continue; //repeat loop
		}
	

	const size_t k = (task.first + task.last)/2; //inbetween position of first and last
	if (task.dim==0) // chooses which dimension will be used, either x or y
		std::nth_element(index + task.first, index + k, index + task.last + 1, lower_x(points));
	else
		std::nth_element(index + task.first, index + k, index + task.last +1, lower_y(points));

	const size_t
		i0 = nodes.size(), i1 = i0 +1; 
	n.split = index[k];
	n.i0 = i0;
	n.i1 = i1;

	const size_t next_dir = task.dim^1;
	const build_task
		task0 = {task.first, k, i0, next_dir}, task1 = {k + 1, task.last, i1, next_dir};
		tasks[current_task] = task0;
		nodes.push_back(node());
		++current_task;
		assert(current_task<stack_size);
		tasks[current_task] = task1;
		nodes.push_back(node());
	}

	while (current_task != 1);
		delete [] index;
		assert(nodes.size()==node_count);
		this->min = min;
		this->max = max;


}

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

struct kd_tree::node // The node structure that will hold the information for the kd-tree
{
	size_t i0, i1, split; // i0 and i1 will note the indexes of the child nodes

	node(): i0(-1), i1(-1), split(-1) // the split point index. split(-1) will refer to a leaf node
	{} 
	friend bool is_leaf(const node &n)
	{ 
		return n.split==size_t(-1);
	}
};

//Constructs for initializing point references
struct lower_x
{
	const std::vector<point> &points;

	lower_x(const std:vector<points> &p) : points(p);
	{}
	bool operator()(size_t i1, size_t i2) const
	//This function looks to see if point i1 is larger than i2
	{
		return points[i1].x<points[i2].x;
	}
};

struct lower_y
{
	const std::vector<point> &points;

	lower_y(const std::vector<points> &p): points(p)
	{}
	bool operator()(size_t i1, size_t i2) const
	{
		return points[i1].x<points[i2].x;
	}
};

// The constructs are each for 1 dimension, either being dimension x or y

/*-----------------------------------------------------------------*/
/* Seperation for Kd-tree class                                    */
/*-----------------------------------------------------------------*/


struct kd_tree;
{
	struct node; 

	point min, max; // will store lower and upper points of the bounding rectangle
	vector<node> nodes;

	kd_tree(const vector<point> &points);
};