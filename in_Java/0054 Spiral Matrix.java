class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if(matrix == null || matrix.length == 0) return res;
        int row = matrix.length;
        int col = matrix[0].length;
        int left = 0, right = col-1;
        int up = 0, down = row-1;
        while(res.size() != row * col){
            for(int j = left; j <= right && res.size() < row*col; j++){
                res.add(matrix[up][j]);
            }
            for(int j = up+1; j < down && res.size() < row*col; j++){
                res.add(matrix[j][right]);
            }
            for(int j = right; j >= left && res.size() < row*col; j--){
                res.add(matrix[down][j]);
            }
            for(int j = down-1; j > up && res.size() < row*col; j--){
                res.add(matrix[j][left]);
            }
            left++; right--;
            up++; down--;
        }
        return res;
    }
}