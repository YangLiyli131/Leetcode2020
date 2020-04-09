class Solution {
    public int repeatedNTimes(int[] A) {
        Set<Integer> h = new HashSet<>();
        int res = A[0];
        for(int i : A){
            if(!h.contains(i)) h.add(i);
            else{
                res = i;
                break;
            }
        }
        return res;
    }
}