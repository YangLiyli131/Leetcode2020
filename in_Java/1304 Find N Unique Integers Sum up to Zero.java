class Solution {
    public int[] sumZero(int n) {
        int[] res = new int[n];
        int id = 0;
        int i = 1;
        while(n > 1){
            res[id] = i;
            res[id+1] = -i;
            id += 2;
            i++;
            n -= 2;
        }
        return res;
    }
}