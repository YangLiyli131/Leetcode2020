class Solution {
    public String convertToTitle(int n) {
        String s = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder sb = new StringBuilder();
        while(n != 0){
            int tail = n % 26;
            if(tail != 0){
                sb.insert(0, s.substring(tail,tail+1));
                n /= 26;
            }else{
                sb.insert(0, s.substring(26,27));
                n = n / 26 - 1;
            }
        }
        return sb.toString();
    }
}