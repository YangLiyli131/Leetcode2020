class Solution {
    public boolean checkRecord(String s) {
        int a = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'A') a++;
            if(i+3 <= s.length() && s.substring(i,i+3).equals("LLL")) return false;
        }
        if(a > 1) return false;
        
        return true;
    }
}