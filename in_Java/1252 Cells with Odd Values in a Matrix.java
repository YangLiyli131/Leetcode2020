class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int[] row = new int[n];
        int[] col = new int[m];
        for(int i = 0; i < indices.length; i++){
            row[indices[i][0]]++;
            col[indices[i][1]]++;
        }
        int res = 0;
        for(int i : row){
            for(int j : col){
                if((i + j) % 2 == 1) res++;
            }
        }
        return res;
    }
}