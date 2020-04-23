class Solution {
    int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        List<List<Integer>> res = new ArrayList<>();
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return res;
        int row = matrix.length, col = matrix[0].length;
        int[][] m1 = new int[row][col];
        int[][] m2 = new int[row][col];
        /*
        for(int i = 0; i < row; i++){
            dfs(matrix,m1,i,0);
            dfs(matrix,m2,i,col-1);
        }
        for(int i = 0; i < col; i++){
            dfs(matrix,m1,0,i);
            dfs(matrix,m2,row-1,i);
        }
        */
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(i == 0 || j == 0){
                    dfs(matrix,m1,i,j);
                }
            }
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(i == row-1 || j == col-1){
                    dfs(matrix,m2,i,j);
                }
            }
        }
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(m1[i][j] == 1 && m2[i][j] == 1){
                    List<Integer> t = new ArrayList<>();
                    t.add(i);t.add(j);
                    res.add(t);
                }
            }
        }
        return res;
    }
    private void dfs(int[][] m, int[][] v, int i, int j){
        v[i][j] = 1;
        for(int[] d : dir){
            int x = i + d[0];
            int y = j + d[1];
            if(x < 0 || y < 0 || x >= m.length || y >= m[0].length || m[i][j] > m[x][y] || v[x][y] == 1) continue;
            dfs(m,v,x,y);
        }
    }
}