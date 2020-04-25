class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[2];
        res[0] = find1(nums,target);
        res[1] = find2(nums,target);
        return res;
    }
    private int find1(int[] nums, int t){
        if(nums == null || nums.length == 0) return -1;
        int i = 0, j = nums.length-1;
        while(i + 1 < j){
            int m = i + (j-i)/2;
            if(nums[m] == t) j = m;
            else if(nums[m] > t) j = m-1;
            else i = m + 1;
        }
        if(nums[i] == t) return i;
        if(nums[j] == t) return j;
        return -1;
    }
    private int find2(int[] nums, int t){
        if(nums == null || nums.length == 0) return -1;
        int i = 0, j = nums.length-1;
        while(i + 1 < j){
            int m = i + (j-i)/2;
            if(nums[m] == t) i = m;
            else if(nums[m] > t) j = m-1;
            else i = m + 1;
        }
        if(nums[j] == t) return j;
        if(nums[i] == t) return i;
        return -1;
    }
}