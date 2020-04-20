class Solution {
    public int singleNonDuplicate(int[] nums) {
        int i;
        int j;
        for(i = 0, j = 1; j < nums.length; i+=2, j+= 2){
            if(nums[i] != nums[j]) return nums[i];
        }
        return nums[i];
    }
}