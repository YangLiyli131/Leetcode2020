class Solution {
    public int uniquePaths(int m, int n) {
        int[][] temp = new int[n][m];
        for(int i = 0; i < m; i++){
            temp[0][i] = 1;
        }
        for(int i = 0; i < n; i++){
            temp[i][0] = 1;
        }
        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                temp[i][j] = temp[i-1][j] + temp[i][j-1];
            }
        }
        return temp[n-1][m-1];
    }
}