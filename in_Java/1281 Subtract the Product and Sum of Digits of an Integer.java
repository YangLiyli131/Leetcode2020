class Solution {
    public int subtractProductAndSum(int n) {
        List<Integer> l = new ArrayList<>();
        while(n != 0){
            l.add(n % 10);
            n /= 10;
        }
        int a = 0;
        int b = 1;
        for(int i : l){
            a += i;
            b *= i;
        }
        return b - a;
    }
}