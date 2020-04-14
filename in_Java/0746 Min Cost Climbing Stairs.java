class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length+1];
        dp[1] = cost[0];
        int i;
        for(i = 2; i < dp.length-1; i++){
            dp[i] = Math.min(dp[i-1],dp[i-2]) + cost[i-1];
        }
        return Math.min(dp[dp.length-2],dp[dp.length-3] + cost[cost.length-1]);
    }
}