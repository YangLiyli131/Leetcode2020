class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        res[res.length-1] = 1;
        for(int i = res.length-2; i >= 0; i--){
            res[i] = res[i+1] * nums[i+1];
        }
        int t = nums[0];
        nums[0] = 1;
        for(int i = 1; i < nums.length; i++){
            int tt = nums[i];
            nums[i] = t;
            t = t * tt;
        }
        for(int i = 0; i < res.length; i++){
            res[i] = res[i] * nums[i];
        }
        return res;
    }
}