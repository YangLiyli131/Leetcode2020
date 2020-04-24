class Solution {
    int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    public int[][] updateMatrix(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int[][] res = new int[row][col];
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 0) res[i][j] = 0;
                else{
                    res[i][j] = bfs(matrix,i,j);
                }
            }
        }
        return res;
    }
    private int bfs(int[][] g, int i, int j){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i,j});
        int n;
        int level = 1;
        while(q.size() != 0){
            n = q.size();
            while(n-- != 0){
                int[] cur = q.poll();
                int a = cur[0], b = cur[1];
                for(int[] d : dir){
                    int x = a + d[0];
                    int y = b + d[1];
                    if(x >= 0 && x < g.length && y >= 0 && y < g[0].length){
                        if(g[x][y] == 0) return level;
                        q.add(new int[]{x,y});
                    }
                }
            }
            level++;
        }
        return level;
    }
}