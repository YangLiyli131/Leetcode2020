class Solution {
    public void moveZeroes(int[] nums) {
        int id = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[id++] = nums[i];
            }
        }
        for(int j = id; j < nums.length; j++){
            nums[j] = 0;
        }
    }
}