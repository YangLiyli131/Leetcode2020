class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : nums) hm.put(i, hm.getOrDefault(i,0)+1);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> (b-a));
        for(int x : hm.values()) pq.add(x);
        int[] res = new int[k];
        int id = 0;
        int kk = k;
        while(k-- != 0) res[id++] = pq.poll();
        for(int i = 0; i < kk; i++){
            int cur = res[i];
            for(int key : hm.keySet()){
                if(hm.get(key) == cur){
                    res[i] = key;
                    hm.remove(key);
                    break;
                }
            } 
        }
        return res;
    }
}