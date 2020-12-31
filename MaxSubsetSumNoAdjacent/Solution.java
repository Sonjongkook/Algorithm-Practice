import java.util.*;

class Program {
  public static int maxSubsetSumNoAdjacent(int[] array) {
    // Write your code here.
		int[] solution = array.clone();
		
		//edge cases
		if(array.length ==0){
			return 0;
		}else if(array.length==1){
			return array[0];
		}
		//base case		
		solution[1] = Math.max(array[0], array[1]);
		//Dynamic programming implemntation
		for(int i=2; i< array.length; i++){
			solution[i] = Math.max((solution[i-2] + array[i]), solution[i-1]);
			
		}
    return solution[array.length-1];
  }
}
