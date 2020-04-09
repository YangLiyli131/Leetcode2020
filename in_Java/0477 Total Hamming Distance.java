class Solution {
    public int totalHammingDistance(int[] nums) {
        int total = 0;
        int n = nums.length;
        for(int i = 0; i < 32; i++){
            int bic = 0;
            for(int j : nums){
                bic += (j >> i) & 1;
            }
            total += bic * (n - bic);
        }
        return total;
    }
}