class Solution {
    public int islandPerimeter(int[][] grid) {
        int n = 0;
        int over = 0;
        int row = grid.length;
        int col = grid[0].length;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(grid[i][j] == 1){
                    n++;
                    if(i != 0 && grid[i-1][j] == 1) over++;
                    if(i != row-1 && grid[i+1][j] == 1) over++;
                    if(j != 0 && grid[i][j-1] == 1) over++;
                    if(j != col-1 && grid[i][j+1] == 1) over++;
                }                
            }
        }
        return 4 * n - over;
    }
}