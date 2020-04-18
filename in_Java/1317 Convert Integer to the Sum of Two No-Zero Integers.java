class Solution {
    public int[] getNoZeroIntegers(int n) {
        int[] res = new int[2];
        for(int i = 1; i < n; i++){
            if(check(i) && check(n - i)){
                res[0] = i;
                res[1] = n-i;
                return res;
            }
        }
        return res;
    }
    private boolean check(int n){
        for(char c : String.valueOf(n).toCharArray()){
            if(c == '0') return false;
        }
        return true;
    }
}