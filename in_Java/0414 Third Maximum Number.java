class Solution {
    public int thirdMax(int[] nums) {
        long a = Long.MIN_VALUE;
        long b = Long.MIN_VALUE;
        long c = Long.MIN_VALUE;
        for(int i : nums){
            if(i > a){
                c = b;
                b = a;
                a = i;
            }else if(i > b && i < a){
                c = b;
                b = i;
            }
            else if(i > c && i < b){
                c = i;
            }
        }
        return (int)(c == Long.MIN_VALUE? a : c);
    }
}