class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        int res = 0;
        int i = 0;
        while(i < nums.length && nums[i] != 1) i++;
        int id = i;
        while(id < nums.length){
            while(i < nums.length && nums[i] == 1){
                i++;
            }
            if(i - id > res) res = i - id;
            id = i+1;
            i++;
        }
        return res;        
    }
}