class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones == null || stones.length == 0) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->(b-a));
        for(int i :stones) pq.add(i);
        while(pq.size() > 1){
            int a = pq.poll();
            int b = pq.poll();
            if(a == b) continue;
            else pq.add(Math.abs(a-b));
        }
        if(pq.size() == 1) return pq.poll();
        else return 0;
    }
}