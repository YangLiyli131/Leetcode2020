class Solution {
    public String freqAlphabets(String s) {
        List<Character> l = new ArrayList<>();
        for(int i = 0; i < s.length(); ){
            if((i+2) < s.length() && s.charAt(i+2) == '#'){
                l.add((char)('a' + (Integer.parseInt(s.substring(i,i+2)) - 1)));
                i += 3;
            }else{
                l.add((char)('a' + (Integer.parseInt(s.substring(i,i+1)) - 1)));
                i++;
            }
        }
        String res = "";
        for(char c : l) res += String.valueOf(c);
        return res;
    }
}