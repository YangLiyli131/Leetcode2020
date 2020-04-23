class Solution {
    public int numEnclaves(int[][] A) {
        // start from the boundary 1s, move inside
        // marker all those reachable 1s to another state
        // scan the matrix again to search for those whose values are still 1
        int row = A.length, col = A[0].length;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(i == 0 || j == 0 || i == row-1 || j == col-1){
                    if(A[i][j] == 1){
                        dfs(A,i,j);
                    }
                }
            }
        }
        int res = 0;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(A[i][j] == 1) res++;
            }
        }
        return res;
    }
    private void dfs(int[][] A, int i, int j){
        if(i < 0 || j < 0 || i >= A.length || j >= A[0].length || A[i][j] == 0 || A[i][j] == -1) return;
        A[i][j] = -1;
        dfs(A,i-1,j);
        dfs(A,i+1,j);
        dfs(A,i,j-1);
        dfs(A,i,j+1);
    }
}