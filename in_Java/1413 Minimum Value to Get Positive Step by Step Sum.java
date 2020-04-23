class Solution {
    public int minStartValue(int[] nums) {
        int[] cumu = new int[nums.length];
        cumu[0] = nums[0];
        int curmin = nums[0];
        for(int i = 1; i < nums.length; i++){
            cumu[i] = cumu[i-1] + nums[i];
            curmin = Math.min(curmin, cumu[i]);
        }
        return (1 - curmin) < 1? 1 : (1-curmin);
    }
}