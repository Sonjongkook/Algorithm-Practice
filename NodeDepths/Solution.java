import java.util.*;

class Program {

  public static int nodeDepths(BinaryTree root) {
		return DepthHelper(root, 0);
    // Write your code here.
  }
	
	public static int DepthHelper(BinaryTree node, int level) {
		if(node == null){
			return 0;
		}
		//Recursive algorithm to get the sum of the node depths 		
		return level + DepthHelper(node.left, level+1) + DepthHelper(node.right, level+1);
	}

  static class BinaryTree {
    int value;
    BinaryTree left;
    BinaryTree right;

    public BinaryTree(int value) {
      this.value = value;
      left = null;
      right = null;
    }
  }
}
