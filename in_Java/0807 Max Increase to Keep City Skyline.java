class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] rowview = new int[grid.length];
        int[] colview = new int[grid[0].length];
        int cur;
        for(int i = 0; i < grid.length; i++){
            cur = Integer.MIN_VALUE;
            for(int j = 0; j < grid[0].length; j++){
                if(cur < grid[i][j]) cur = grid[i][j];
            }
            rowview[i] = cur;
        }
        for(int i = 0; i < grid[0].length; i++){
            cur = Integer.MIN_VALUE;
            for(int j = 0; j < grid.length; j++){
                if(cur < grid[j][i]) cur = grid[j][i];
            }
            colview[i] = cur;
        }
        int res = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                res += Math.min(rowview[i],colview[j]) - grid[i][j];
            }
        }
        return res;
    }
}