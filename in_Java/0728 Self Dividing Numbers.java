class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<>();
        for(int i = left; i <= right; i++){
            if(check(i)) res.add(i);
        }
        return res;
    }
    private boolean check(int n){
        int back = n;
        while(back != 0){
            int t = back % 10;
            if(t == 0) return false;
            if(n % t != 0) return false;
            back /= 10;
        }
        return true;
    }
}