class Solution {
    public int projectionArea(int[][] grid) {
        int res = 0;
        int row = grid.length;
        int col = grid[0].length;
        for(int r = 0; r < row; r++){
            int rowmax = 0;
            for(int c = 0; c < col; c++){
                if(rowmax < grid[r][c]){
                    rowmax = grid[r][c];
                }
            }
            res += rowmax;
        }
        for(int c = 0; c < col; c++){
            int colmax = 0;
            for(int r = 0; r < row; r++){
                if(colmax < grid[r][c]){
                    colmax = grid[r][c];
                }
            }
            res += colmax;
        }
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                if(grid[r][c] != 0) res++;
            }
        }
        return res;
    }
}