class Solution {
    public int findNumbers(int[] nums) {
        int res = 0;
        for(int i : nums){
            if(i > 9 && helper(i)) res++;
        }
        return res;
    }
    private boolean helper(int n){
        int t = 0;
        while(n != 0){
            n /= 10;
            t++;
        }
        return t % 2 == 0;
    }
}