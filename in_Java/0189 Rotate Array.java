class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        rev(nums, 0, nums.length-1);
        rev(nums, 0, k-1);
        rev(nums, k, nums.length-1);
    }
    private void rev(int[] nums, int i, int j){
        int t;
        while(i < j){
            t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
            i++;
            j--;
        }
    }
}