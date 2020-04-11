class Solution {
    public String alphabetBoardPath(String target) {
        String res = "";
        int[] curpos = new int[]{0,0};
        Map<Character, int[]> hm = new HashMap<>();
        String[] board = new String[]{"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"};
        String s;
        for(int i = 0; i < board.length; i++){
            s = board[i];
            for(int j = 0; j < s.length(); j++){
                hm.put(s.charAt(j), new int[]{i,j});
            }
        }
        int[] id;
        int xdis;
        int ydis;
        for(char c : target.toCharArray()){
            id = hm.get(c);
            if(id[0] == curpos[0] && id[1] == curpos[1]) res += "!";
            else{
                xdis = id[0] - curpos[0];
                ydis = id[1] - curpos[1];
                
                while(xdis < 0){
                    res += "U";
                    xdis++;
                }
                while(ydis < 0){
                    res += "L";
                    ydis++;
                }
                while(xdis > 0){
                    res += "D";
                    xdis--;
                }
                while(ydis > 0){
                    res += "R";
                    ydis--;
                }
                res += "!";
            }
            curpos = id;
        }
        return res;
    }
}