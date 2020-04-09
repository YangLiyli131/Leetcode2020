class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> hs = new HashSet<>();
        int t;
        while(true){
            t = 0;
            while(n != 0){
                t += (n % 10) * (n % 10);
                n /= 10;
            }
            if(hs.contains(t)) return false;
            else if(t == 1) return true;
            else hs.add(t);
            n = t;
        }
    }
}