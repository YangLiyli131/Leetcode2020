class Solution {
    public int search(int[] nums, int target) {
        if(nums == null || nums.length == 0) return -1;
        if(nums.length == 1){
            if(nums[0] == target) return 0;
            else return -1;
        }
        int i = 0; int j= nums.length-1;
        while(i <= j){
            int m = i + (j-i)/2;
            if(nums[m] == target) return m;
            if(nums[i] == target) return i;
            if(nums[j] == target) return j;
            if(nums[i] < nums[m]){
                if(target < nums[m] && target > nums[i]) j = m-1;
                else i = m + 1;
            }else{
                if(target > nums[m] && target < nums[j]) i = m + 1;
                else j = m - 1;
            }
    
        }
        return -1;
    }
}