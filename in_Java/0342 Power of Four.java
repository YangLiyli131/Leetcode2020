class Solution {
    public boolean isPowerOfFour(int num) {
        if(num < 0) return false;
        int count_zero = 0;
        int count_one = 0;
        while(num != 0){
            if(num % 2 == 0) count_zero++;
            else count_one++;
            num/=2;
        }
        if(count_one == 1 && count_zero % 2 == 0) return true;
        else return false;
    }
}