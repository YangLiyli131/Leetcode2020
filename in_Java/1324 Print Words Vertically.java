class Solution {
    public List<String> printVertically(String s) {
        String[] str = s.split(" ");
        int maxlen = 0;
        for(String x : str){
            if(maxlen < x.length()) maxlen = x.length();
        }
        char[][] t = new char[str.length][maxlen];
        for(int i = 0; i < str.length; i++){
            for(int j = 0; j < maxlen; j++){
                t[i][j] = ' ';
            }
        }
        for(int i = 0; i < str.length; i++){
            String cur = str[i];
            for(int j = 0; j < cur.length(); j++){
                t[i][j] = cur.charAt(j);
            }
        }
        List<String> res = new ArrayList<>();
        String temp;
        for(int c = 0; c < maxlen; c++){
            temp = "";
            for(int r = 0; r < str.length; r++){
                if(t[r][c] == ' ') temp += " ";
                else temp += String.valueOf(t[r][c]);
            }
            res.add(removeT(temp));
        }
        return res;
    }
    private String removeT(String s){
        int n = s.length()-1;
        while(s.charAt(n) == ' '){
            n--;
        }
        return s.substring(0,n+1);
    }
}