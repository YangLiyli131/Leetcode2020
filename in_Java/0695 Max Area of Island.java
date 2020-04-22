class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxres = Integer.MIN_VALUE;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    int cur = dfs(grid,i,j);
                    maxres = Math.max(cur,maxres);
                }
            }
        }
        return maxres == Integer.MIN_VALUE? 0 : maxres;
    }
    private int dfs(int[][] g, int i, int j){
        int n = 0;
        if(i < 0 || j < 0 || i >= g.length || j >= g[0].length || g[i][j] != 1) return 0;
        g[i][j] = -1;
        n++;
        n += dfs(g,i-1,j);
        n += dfs(g,i+1,j);
        n += dfs(g,i,j-1);
        n += dfs(g,i,j+1);
        return n;
    }
}