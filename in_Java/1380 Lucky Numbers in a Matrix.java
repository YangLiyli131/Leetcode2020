class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int[] rowmin = new int[row];
        int[] colmax = new int[col];
        int curmin;
        int curmax;
        for(int r = 0; r < row; r++){
            curmin = Integer.MAX_VALUE;
            for(int c = 0; c < col; c++){
                if(curmin > matrix[r][c]){
                    curmin = matrix[r][c];
                }
            }
            rowmin[r] = curmin;
        }
        for(int c = 0; c < col; c++){
            curmax = Integer.MIN_VALUE;
            for(int r = 0; r < row; r++){
                if(curmax < matrix[r][c]){
                    curmax = matrix[r][c];
                }
            }
            colmax[c] = curmax;
        }
        List<Integer> res = new ArrayList<>();
        List<Integer> t = new ArrayList<>();
        for(int i : colmax) t.add(i);
        for(int i : rowmin){
            if(t.contains(i)){
                res.add(i);
            }
        }
        return res;
    }
}