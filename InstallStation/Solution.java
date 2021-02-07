class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int position = 1;
        int station_idx= 0;
        
        while(position <= n){

            if(station_idx < stations.length && position >= stations[station_idx] - w){
                position = stations[station_idx] + w + 1;
                station_idx++;
            }else{
                answer+=1;
                position += w*2 + 1;
            }    
        }
        return answer;
    }
}
