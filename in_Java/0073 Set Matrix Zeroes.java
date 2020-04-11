class Solution {
    public void setZeroes(int[][] matrix) {
        boolean clear_firstrow = false;
        boolean clear_firstcol = false;
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][0] == 0){
                clear_firstcol = true;
                break;
            }
        }
        for(int i = 0; i < matrix[0].length; i++){
            if(matrix[0][i] == 0){
                clear_firstrow = true;
                break;
            }
        }        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i = 1; i < matrix.length; i++){
            if(matrix[i][0] == 0){
                for(int j = 0; j < matrix[0].length; j++){
                    matrix[i][j] = 0;
                }
            }
        }
        for(int i = 1; i < matrix[0].length; i++){
            if(matrix[0][i] == 0){
                for(int j = 0; j < matrix.length; j++){
                    matrix[j][i] = 0;
                }
            }
        }
        if(clear_firstcol){
            for(int i = 0; i < matrix.length; i++){
                matrix[i][0] = 0;
            }
        }
        if(clear_firstrow){
            for(int i = 0; i < matrix[0].length; i++){
                matrix[0][i] = 0;
            }
        }
    }
}