class Solution {
    public boolean judgeCircle(String moves) {
        char[] ch = moves.toCharArray();
        int x = 0;
        int y = 0;
        for(char c : ch){
            if(c == 'U') x += 1;
            else if (c == 'D') x -= 1;
            else if (c == 'L') y -= 1;
            else y += 1;
        }
        return x == 0 && y == 0;
    }
}