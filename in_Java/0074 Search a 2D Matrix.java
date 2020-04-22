class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int row = matrix.length, col = matrix[0].length;
        int id = 0;
        for(int i = 0; i < row; i++){
            if(matrix[i][col-1] == target) return true;
            if(matrix[i][col-1] > target){
                id = i;
                break;
            }
        }
        int[] arr = matrix[id];
        int left = 0, right = col-1;
        while(left <= right){
            int m = left + (right-left)/2;
            if(arr[m] == target) return true;
            else if(arr[m] < target) left = m+1;
            else right = m-1;
        }
        return false;
    }
}