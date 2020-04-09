class Solution {
    public int climbStairs(int n) {
        int[] t = new int[n+1];
        t[0] = 1;
        t[1] = 1;
        for(int i = 2; i <= n; i++){
            t[i] = t[i-2] + t[i-1];
        }
        return t[n];
    }
}