class Solution {
    public int[] numberOfLines(int[] widths, String S) {
        int[] res = new int[2];
        if(S == null || S.length() == 0) return res;
        int curlen = 0;
        int lines = 1;
        for(char c : S.toCharArray()){
            int idx = widths[c - 'a'];
            if(curlen + idx <= 100){
                curlen += idx;
            }else{
                curlen = idx;
                lines++;
            }
        }
        res[0] = lines;
        res[1] = curlen;
        return res;
    }
}