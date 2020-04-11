class Solution {
    public int searchInsert(int[] nums, int target) {
        int[] res = new int[nums.length+1];
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == target) return i;
            res[i] = nums[i];
        }
        res[res.length-1] = target;
        Arrays.sort(res);
        for(int i = 0; i < res.length; i++){
            if(res[i] == target) return i;
        }
        return -1;
    }
}