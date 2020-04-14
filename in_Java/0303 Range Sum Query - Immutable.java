class NumArray {
    int[] cursum;
    public NumArray(int[] nums) {
        cursum = new int[nums.length+1];
        for(int i = 1; i < cursum.length; i++){
            cursum[i] = cursum[i-1] + nums[i-1];
        }
    }
    
    public int sumRange(int i, int j) {
        return cursum[j+1] - cursum[i];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */