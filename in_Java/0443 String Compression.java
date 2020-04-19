class Solution {
    public int compress(char[] chars) {
        int id = 0;
        int curlen;
        int i = 0, j = 0;
        while(j < chars.length){
            while(j < chars.length && chars[i] == chars[j]) j++;
            curlen = j - i;
            if(curlen == 1){
                chars[id] = chars[i];
                id++;
            }
            else{
                chars[id] = chars[i];
                char[] t = String.valueOf(curlen).toCharArray();
                int L = 0;
                while(L < t.length) chars[++id] = t[L++];
                id++;
            }
            i = j;
        }
        return id;
    }
}