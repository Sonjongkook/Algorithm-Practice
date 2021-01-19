# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate(node, cursum, sums):
	if node is None:
		return
	
	new_cursum = cursum + node.value
	if node.left is None and node.right is None:
		sums.append(new_cursum)
		return
		
	calculate(node.left, new_cursum, sums)
	calculate(node.right, new_cursum, sums)		
		
def branchSums(root):
	sums = []
	calculate(root, 0, sums)
	return sums

    # Write your code here.
    pass
