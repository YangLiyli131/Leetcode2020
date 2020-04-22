class Solution {
    public boolean canJump(int[] nums) {
        int[] dp = new int[nums.length];
        if(nums.length == 1) return true;
        if(nums[0] == 0) return false;
        int steps;
        dp[0] = 1;
        for(int i = 0; i < nums.length-1; i++){
            steps = nums[i];
            if(dp[i] != 0){           
                for(int x = 1; x <= steps; x++){
                    if(i+x < nums.length) dp[i+x] = 1;
                }
                if(dp[nums.length-1] == 1) return true;
            }
        }
        return dp[nums.length-1] == 1;
    }
}