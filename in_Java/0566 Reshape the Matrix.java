class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        if(nums == null || nums.length == 0 || nums[0].length == 0) return nums;
        int row = nums.length;
        int col = nums[0].length; 
        if(row * col != r * c) return nums;
        int[] n = new int[r*c];
        int id = 0;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                n[id++] = nums[i][j];
            }
        }
        int[][] res = new int[r][c];
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                res[i][j] = n[j+i*c];
            }
        }
        return res;
    }
}