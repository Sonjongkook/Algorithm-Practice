import java.util.*;

class Program {
  public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
    // Write your code here.
		

		List<Integer[]> Answer = new ArrayList<Integer[]>();;
		
		Arrays.sort(array);
		//Iterate the array except last two elements considering pointers 		
		for (int i=0; i< array.length-2; i++){
			// initialize pointer  			
			int left_pointer = i+1;
			int right_pointer = array.length -1;
			
			while (true){
				Integer[] subanswer = new Integer[3];
				//if the sum of three elements is less than target sum then move the left pointer to right 				
				if(array[i] + array[left_pointer] + array[right_pointer] < targetSum){
					left_pointer++;
				//if the sum of three elements is more than target sum then move the right pointer to left 		
				}else if(array[i] + array[left_pointer] + array[right_pointer] > targetSum){
					right_pointer--;
				}else{
					//If the target sum and three elments sum is equal then store it to the sub answer and add it to the answer					
					subanswer[0] = array[i];
					subanswer[1] = array[left_pointer];
					subanswer[2] = array[right_pointer];
					Answer.add(subanswer);
					//Two cases when sum is equal 
					//If there is no element between pointers end the iterate
					if(right_pointer-left_pointer == 1){
						break;
					}else{
					//If there is element between pointers then look through it 						
						left_pointer++;
						right_pointer--;
					}
				}
				if(left_pointer == right_pointer){
					break;
				}
			}
		}
    return Answer;
  }
}
