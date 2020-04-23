class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i = 0; i < points.length; i++){
            hm.put(i, points[i][0] * points[i][0] + points[i][1] * points[i][1]);
        }
        PriorityQueue<Map.Entry<Integer,Integer>> pq = new PriorityQueue<>((i,j) -> i.getValue() - j.getValue());
        pq.addAll(hm.entrySet());
        int[][] res = new int[K][2];
        int id = 0;
        while(K-- != 0){
            int cur = pq.poll().getKey();
            res[id][0] = points[cur][0];
            res[id++][1] = points[cur][1];
        }
        return res;
    }
}