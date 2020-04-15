class Solution {
    public int search(int[] nums, int target) {
        int i = 0; 
        int j = nums.length-1;
        int m;
        while(i < j){
            m = i + (j-i)/2;
            if(nums[m] == target) return m;
            else if(nums[m] < target) i = m + 1;
            else j = m;
        }
        if(nums[i] == target) return i;
        return -1;
    }
}