class Solution {
    public int reverse(int x) {
        int res = 0;
        while(x != 0){
            int end = x % 10;
            int newres = res * 10 + end;
            if((newres - end) / 10 != res) return 0;
            res = newres;
            x /= 10;
        }
        return res;
    }
}