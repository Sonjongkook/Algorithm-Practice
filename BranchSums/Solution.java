import java.util.*;

class Program {
  // This is the class of the input root. Do not edit it.
  public static class BinaryTree {
    int value;
    BinaryTree left;
    BinaryTree right;

    BinaryTree(int value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
	
  public static List<Integer> branchSums(BinaryTree root) {
    // Write your code here.
		List<Integer> Sums = new ArrayList<Integer>();
		calBranchSums(root, 0, Sums);
		
    return Sums;
  }
	
	public static void calBranchSums(BinaryTree tree, int RunningSum, List<Integer> Sums){
		
		if(tree == null){
			return;
		}
		
		int newRunningSum = RunningSum + tree.value;
		
		if(tree.left == null && tree.right == null){
			Sums.add(newRunningSum);
			return;
		}
		calBranchSums(tree.left, newRunningSum, Sums);
		calBranchSums(tree.right, newRunningSum, Sums);
		
	}
	
}
