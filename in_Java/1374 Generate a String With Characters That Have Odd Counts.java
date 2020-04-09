class Solution {
    public String generateTheString(int n) {
        String res = "";
        if(n % 2 == 0){
            res += "a";
            while(n != 1){
                res += "b";
                n--;
            }
        }else{
            while(n != 0){
                res += "a";
                n--;
            }
        }
        return res;
    }
}