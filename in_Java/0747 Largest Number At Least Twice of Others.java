class Solution {
    public int dominantIndex(int[] nums) {
        if(nums == null || nums.length == 0) return -1;
        int first = Integer.MIN_VALUE;
        int res = 0;
        int second = Integer.MIN_VALUE;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > first) {second = first; first = nums[i]; res = i;}
            else if(nums[i] > second) second = nums[i];
            else continue;
        }
        //System.out.println(first);
        //System.out.println(second);
        if(first >= second * 2) return res;
        else return -1;
    }
}