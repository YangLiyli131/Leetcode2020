class Solution {
    public int countNegatives(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int row = grid.length;
        int col = grid[0].length;
        int res = 0;
        for(int i = 0; i < row; i++){
            int[] cur = grid[i];
            int left = 0, right = col-1;
            if(cur[right] >= 0) continue;
            if(cur[left] < 0){
                res += col;
                continue;
            }
            // find first negative in this row
            while(left < right){
                int m = left + (right-left)/2;
                if(cur[m] >=0) left = m+1;
                else right = m;
            }
            res += col - left;
        }
        return res;
    }
}