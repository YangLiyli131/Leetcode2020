import java.util.Random; 
class Solution {
    int[] arr;
    int[] backup;
    public Solution(int[] nums) {
        arr = new int[nums.length];
        backup = new int[nums.length];
        for(int i = 0; i < nums.length; i++) arr[i] = nums[i];
        for(int i = 0; i < nums.length; i++) backup[i] = nums[i];
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return backup;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        Random r = new Random();
        for(int j = arr.length-1; j > 0; j--){
            int i = r.nextInt(j+1);
            int t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
        }
        return arr;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */