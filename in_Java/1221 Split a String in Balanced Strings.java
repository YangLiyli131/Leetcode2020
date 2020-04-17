class Solution {
    public int balancedStringSplit(String s) {
        int res = 0;
        int cur = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'L') cur--;
            else cur++;
            if(cur == 0){
                res++;
            }
        }
        return res;
    }
}