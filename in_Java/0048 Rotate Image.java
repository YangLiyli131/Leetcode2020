class Solution {
    public void rotate(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        for(int i = 0; i < row; i++){
            for(int j = i+1; j < col; j++){
                int t = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = t;
            }
        }
        int i = 0;
        int j = col - 1;
        while(i < j){
            for(int id = 0; id < row; id++){
                int t = matrix[id][i];
                matrix[id][i] = matrix[id][j];
                matrix[id][j] = t;
            }
            i++; 
            j--;
        }
    }
}