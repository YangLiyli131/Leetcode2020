class Solution {
    public boolean isValidSudoku(char[][] board) {
        int row = board.length;
        int col = board[0].length;
        
        for(int r = 0; r < row; r++){
            HashSet<Character> hs = new HashSet<>();
            for(int c = 0; c < col; c++){
                if(board[r][c] != '.'){
                    if(hs.contains(board[r][c])) return false;
                    else hs.add(board[r][c]);
                }
            }
        }
        for(int c = 0; c < col; c++){
            HashSet<Character> hs = new HashSet<>();
            for(int r = 0; r < row; r++){
                if(board[r][c] != '.'){
                    if(hs.contains(board[r][c])) return false;
                    else hs.add(board[r][c]);
                }
            }
        }
        HashSet<Character> hs = new HashSet<>();
        for(int i = 0; i <= 2; i++){
            for(int j = 0; j <= 2; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 0; i <= 2; i++){
            for(int j = 3; j <= 5; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 0; i <= 2; i++){
            for(int j = 6; j <= 8; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 3; i <= 5; i++){
            for(int j = 0; j <= 2; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 3; i <= 5; i++){
            for(int j = 3; j <= 5; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 3; i <= 5; i++){
            for(int j = 6; j <= 8; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 6; i <= 8; i++){
            for(int j = 0; j <= 2; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 6; i <= 8; i++){
            for(int j = 3; j <= 5; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        hs = new HashSet<>();
        for(int i = 6; i <= 8; i++){
            for(int j = 6; j <= 8; j++){
                if(board[i][j] != '.'){
                    if(hs.contains(board[i][j])) return false;
                    else hs.add(board[i][j]);
                }
            }
        }
        return true;
    }
}