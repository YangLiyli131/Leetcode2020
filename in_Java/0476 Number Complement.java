class Solution {
    public int findComplement(int num) {
        int res = 0;
        int p = 0;
        int t;
        while(num != 0){
            t = num % 2;
            if(t == 0){
                res += Math.pow(2,p);
            }
            p++;
            num /= 2;
        }
        return res;
    }
}