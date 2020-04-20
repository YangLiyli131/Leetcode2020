class Solution {
    public int titleToNumber(String s) {
        int res = 0;
        int p = 0;
        for(int i = s.length()-1; i >= 0; i--){
            int cur = s.charAt(i) - 'A' + 1;
            res += cur * Math.pow(26,p++);
        }
        return res;
    }
}