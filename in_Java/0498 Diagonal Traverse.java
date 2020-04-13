class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return new int[0];
        int row = matrix.length;
        int col = matrix[0].length;
        int[] res = new int[row * col];
        List<Integer> L;
        int id = 1;
        int idx = 0;
        int cur_row;
        int cur_col;
        for(int i = 0; i < row; i++){
            cur_row = i;
            cur_col = 0;         
            L = new ArrayList<Integer>();
            while(cur_row >= 0 && cur_col < col){
                L.add(matrix[cur_row][cur_col]);
                cur_row--;
                cur_col++;
            }
            if(id % 2 == 1){
                for(int item : L) res[idx++] = item;
            }else{
                for(int h = L.size()-1; h >= 0; h--) res[idx++] = L.get(h);
            }
            id++;
        }
        for(int i = 1; i < col; i++){
            cur_row = row-1;
            cur_col = i;         
            L = new ArrayList<Integer>();
            while(cur_row >= 0 && cur_col < col){
                L.add(matrix[cur_row][cur_col]);
                cur_row--;
                cur_col++;
            }
            if(id % 2 == 1){
                for(int item : L) res[idx++] = item;
            }else{
                for(int h = L.size()-1; h >= 0; h--) res[idx++] = L.get(h);
            }
            id++;
        }
        return res;
    }
}