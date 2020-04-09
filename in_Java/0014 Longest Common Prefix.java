class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = "";
        if(strs == null || strs.length == 0) return res;
        int minlen = strs[0].length();
        for(String s : strs){
            if(minlen > s.length()){
                minlen = s.length();
            }
        }
        boolean flag;
        for(int i = 0; i < minlen; i++){
            flag = false;
            char x = strs[0].charAt(i);
            for(int j = 1; j < strs.length; j++){
                if(strs[j].charAt(i) != x){
                    flag = true;
                    break;
                }
            }
            if(!flag){
                res += Character.toString(x);
            }else{
                break;
            }
        }
        return res;
    }
}