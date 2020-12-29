import java.util.*;

//Solution1
class Program {
  public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo) {
    // Write your code here.
		int[] answer = new int[2];
		int smallest_dif = 99999;

		//Sort both arrays
		Arrays.sort(arrayOne);
		Arrays.sort(arrayTwo);
			
		for(int i=0; i<arrayOne.length; i++){
			int dif = 0;
			for(int k=0; k<arrayTwo.length; k++){
				if(k ==0){
					dif = Math.abs(arrayOne[i] - arrayTwo[k]);
				}else{
					if(dif < Math.abs(arrayOne[i] - arrayTwo[k])){
						if(smallest_dif > Math.abs(arrayOne[i] - arrayTwo[k-1])){
							answer[0] = arrayOne[i];
							answer[1] = arrayTwo[k-1];
							smallest_dif = Math.abs(arrayOne[i] - arrayTwo[k-1]);
							break;
						}else{
							break;
						}
					}else{
						dif = Math.abs(arrayOne[i] - arrayTwo[k]);
						if (k== arrayTwo.length-1 && dif < smallest_dif){
							answer[0] = arrayOne[i];
							answer[1] = arrayTwo[k];
							smallest_dif =  Math.abs(arrayOne[i] - arrayTwo[k]);
						}
					}
				}
			}
		}
    return answer;
  }
}

//Solution 2
class Program {
  public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo) {
    // Write your code here.
		int[] answer = new int[2];
		int smallest_dif = 99999;

		//Sort both arrays
		Arrays.sort(arrayOne);
		Arrays.sort(arrayTwo);
			
		for(int i=0; i<arrayOne.length; i++){
			int dif = 0;
			for(int k=0; k<arrayTwo.length; k++){
				if(k ==0){
					dif = Math.abs(arrayOne[i] - arrayTwo[k]);
				}else{
					if(dif < Math.abs(arrayOne[i] - arrayTwo[k])){
						if(smallest_dif > Math.abs(arrayOne[i] - arrayTwo[k-1])){
							answer[0] = arrayOne[i];
							answer[1] = arrayTwo[k-1];
							smallest_dif = Math.abs(arrayOne[i] - arrayTwo[k-1]);
							break;
						}else{
							break;
						}
					}else{
						dif = Math.abs(arrayOne[i] - arrayTwo[k]);
						if (k== arrayTwo.length-1 && dif < smallest_dif){
							answer[0] = arrayOne[i];
							answer[1] = arrayTwo[k];
							smallest_dif =  Math.abs(arrayOne[i] - arrayTwo[k]);
						}
					}
				}
			}
		}
    return answer;
  }
}

