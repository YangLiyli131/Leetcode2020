class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : nums){
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i, hm.get(i)+1);
        }
        List<Integer> L = new ArrayList<>();
        int freq = Integer.MIN_VALUE;
        for(int i : hm.values()){
            if(i > freq) freq = i;
        }
        for(int k : hm.keySet()){
            if(hm.get(k) == freq) L.add(k);
        }
        int res = Integer.MAX_VALUE;
        int[] x;
        for(int i : L){
            x = idxOf(nums,i);
            if(res > x[1] - x[0]) res = x[1] - x[0];
        }
        return res+1;
    }
    private int[] idxOf(int[] n, int i){
        int[] res = new int[2];
        int id = 0;
        while(n[id] != i){
            id++;
        }
        res[0] = id;
        int last = n.length-1;
        while(n[last] != i){
            last--;
        }
        res[1] = last;
        return res;
    }
}