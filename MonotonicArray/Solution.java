import java.util.*;

class Program {
  public static boolean isMonotonic(int[] array) {
    // Write your code here.
		boolean check_mon=true;
		
		//Non increasing case
		for(int i=1; i< array.length; i++){
			if(array[i-1] < array[i]){
				check_mon = false;
			}
		}
		if (check_mon == true){
			return true;
		}else{
			//Non decreasing case
			//initialize boolean value
			check_mon = true;
			for(int i=1; i< array.length; i++){
				if(array[i-1] > array[i]){
					check_mon = false;
				}
			}
			return check_mon;
		}
	}
}
