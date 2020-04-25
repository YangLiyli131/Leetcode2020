class Solution {
    int[][] dir = {{0,1},{0,-1},{1,0},{-1,0},{1,1},{-1,-1},{1,-1},{-1,1}};
    public void gameOfLife(int[][] board) {
        int row = board.length, col = board[0].length;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                board[i][j] = help(board,i,j);
            }
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(board[i][j] == 2) board[i][j] = 0;
                if(board[i][j] == -2) board[i][j] = 1;
            }
        }
        //return board;
    }
    private int help(int[][] g, int i, int j){
        int num_ones = 0;
        int cur = g[i][j];
        for(int[] e : dir){
            int x = i + e[0];
            int y = j + e[1];
            if(x >= 0 && y >= 0 && x < g.length && y < g[0].length){
                if(g[x][y] > 0) num_ones++;
            }
        }
        if(cur == 0 && num_ones == 3) return -2;
        if(cur == 1 && num_ones > 3) return 2;
        if(cur == 1 && num_ones < 2) return 2;
        else return cur;
    }
}