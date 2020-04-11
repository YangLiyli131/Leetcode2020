class Solution {
    public String addBinary(String a, String b) {
        char[] ch_a = a.toCharArray();
        char[] ch_b = b.toCharArray();
        StringBuilder sb = new StringBuilder();
        int i = a.length()-1;
        int j = b.length()-1;
        int over = 0;
        int cur;
        int x;
        int y;
        while(i >= 0 || j >= 0){
            x = (i < 0)? 0 : Character.getNumericValue(ch_a[i]);
            y = (j < 0)? 0 : Character.getNumericValue(ch_b[j]);
            cur = x + y + over;
            over = cur / 2;
            cur = cur % 2;
            sb.insert(0,String.valueOf(cur));
            i--;
            j--;
        }
        String res = sb.toString();
        if(over == 1) return "1" + res;
        else return res;
    }
}