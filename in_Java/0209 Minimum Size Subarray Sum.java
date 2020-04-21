class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int res = Integer.MAX_VALUE;
        for(int i = 0; i < nums.length; i++){
            int j = i;
            int cur = 0;
            while(j < nums.length && cur < s){
                cur += nums[j];
                j++;
            }
            if(cur >= s) res = Math.min(res, j - i);
        }
        return res == Integer.MAX_VALUE? 0 : res;
    }
}

class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        int i = 0, j = 0, m = Integer.MAX_VALUE;
        int ss = 0;
        while(j < nums.length){
            ss += nums[j++];
            while(ss >= s){
                m = Math.min(m, j - i);
                ss -= nums[i++];
            }
        }
        return m == Integer.MAX_VALUE? 0 : m;
    }
}