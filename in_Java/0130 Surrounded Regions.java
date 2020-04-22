class Solution {
    // start from the 'O' on boarder and go inward
    public void solve(char[][] board) {
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(i == 0 || j == 0 || i == board.length-1 || j == board[0].length-1){
                    if(board[i][j] == 'O') dfs(board,i,j);
                }
            }
        }
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == '*') board[i][j] = 'O';
            }
        }
    }
    private void dfs(char[][] g, int i, int j){
        if(i < 0 || j < 0 || i >= g.length || j >= g[0].length || g[i][j] == 'X' || g[i][j] == '*') return;
        g[i][j] = '*';
        dfs(g,i-1,j);
        dfs(g,i+1,j);
        dfs(g,i,j-1);
        dfs(g,i,j+1);        
    }
}