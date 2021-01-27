import java.util.*;

class Program {
  public static int numberOfWaysToMakeChange(int n, int[] denoms) {
    // Write your code here.
		int[] solution = new int[n+1];
		solution[0] = 1;
		
		for (int denom : denoms){
			for (int amount=1; amount < n+1; amount++){
				if(denom <= amount){
					solution[amount] +=  solution[amount - denom];
				}
				System.out.println("amount" + amount);
			}
			System.out.println("denom" + denom);
		}
		return solution[n];
  }
}
