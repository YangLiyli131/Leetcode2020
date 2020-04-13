class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1) return 1;
        int i = 0;
        int j = 0;
        while(j < nums.length){
            while(j < nums.length && nums[i] == nums[j]) j++;
            if(j < nums.length) nums[++i] = nums[j];
        }
        return i+1;
    }
}