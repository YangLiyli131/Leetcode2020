class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int row = A.length;
        int col = A[0].length;
        int i;
        int j;
        for(int r = 0; r < row; r++){
            i = 0;
            j = col - 1;
            while(i <= j){
                if(A[r][i] == A[r][j] && i != j){
                    A[r][i] = A[r][i] == 1? 0 : 1;
                    A[r][j] = A[r][j] == 1? 0 : 1;
                }
                if(A[r][i] == A[r][j] && i == j){
                    A[r][i] = A[r][i] == 1? 0 : 1;
                }
                i++;
                j--;
            }
        }
        return A;
    }
}