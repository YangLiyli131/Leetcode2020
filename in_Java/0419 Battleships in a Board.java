class Solution {
    public int countBattleships(char[][] board) {
        int res = 0;
        int r;
        int c;
        boolean[][] visited = new boolean[board.length][board[0].length];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'X' && !visited[i][j]){
                    res++;
                    r = i;
                    c = j;
                    while(r < board.length && board[r][j] == 'X'){
                        visited[r][j] = true;
                        r++;
                    }
                    while(c < board[0].length && board[i][c] == 'X'){
                        visited[i][c] = true;
                        c++;
                    }
                }
            }
        }
        return res;
    }
}