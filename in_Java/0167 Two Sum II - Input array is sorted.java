class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length-1;
        int t;
        int[] res = new int[2];
        while(i < j){
            t = numbers[i] + numbers[j];
            if(t == target){
                res[0] = i+1;
                res[1] = j+1;
                break;
            }else if(t < target){
                i++;
            }else{
                j--;
            }
        }
        return res;
    }
}