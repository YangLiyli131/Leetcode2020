class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];
        int[] a1 = new int[nums.length-1];
        int[] a2 = new int[nums.length-1];
        for(int i = 0; i < a1.length; i++){
            a1[i] = nums[i];
            a2[i] = nums[i+1];
        }
        int[] dp1 = new int[a1.length+1];
        int[] dp2 = new int[a2.length+1];
        dp1[1] = a1[0];
        dp2[1] = a2[0];
        for(int i = 2; i < dp1.length; i++){
            dp1[i] = Math.max(dp1[i-1], dp1[i-2] + a1[i-1]);
            dp2[i] = Math.max(dp2[i-1], dp2[i-2] + a2[i-1]);
        }
        return Math.max(dp1[dp1.length-1], dp2[dp2.length-1]);
    }
}