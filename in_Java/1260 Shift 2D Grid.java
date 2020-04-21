class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int row = grid.length;
        int col = grid[0].length;
        int[] t = new int[row*col];
        int id = 0;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                t[id++] = grid[i][j];
            }
        }
        k = k % t.length;
        int[] tt = new int[t.length];        
        for(int i = 0; i < k; i++){
            tt[i] = t[t.length-k+i];
        }
        for(int i = k; i < t.length; i++){
            tt[i] = t[i-k];
        }
        id = 0;
        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < row; i++){
            List<Integer> cur = new ArrayList<>();
            for(int j = 0; j < col; j++){
                cur.add(tt[id++]);
            }
            res.add(cur);
        }
        return res;
    }
}