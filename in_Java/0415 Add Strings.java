class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        char[] a = num1.toCharArray();
        char[] b = num2.toCharArray();
        int over = 0;
        int i = a.length-1;
        int j = b.length-1;
        int x;
        int y;
        int cur;
        while(i >= 0 || j >= 0){
            x = i < 0? 0 : (a[i] - '0');
            y = j < 0? 0 : (b[j] - '0');
            cur = x + y + over;
            over = cur / 10;
            cur %= 10;
            sb.insert(0, String.valueOf(cur));
            i--;
            j--;
        }
        String res = sb.toString();
        if(over == 1) res = "1" + res;
        return res;
    }
}