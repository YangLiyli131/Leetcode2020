class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int res = 0;
        if(points.length < 3) return res;
        Map<Integer,Integer> hm;
        for(int i = 0; i < points.length; i++){
            hm = new HashMap<>();
            int a = points[i][0], b = points[i][1];
            for(int j = 0; j < points.length; j++){
                if(i == j) continue;
                int aa = points[j][0], bb = points[j][1];
                int dis = (aa-a) * (aa-a) + (bb-b) * (bb-b);
                hm.put(dis, hm.getOrDefault(dis,0)+1);
            }
            for(int v : hm.values()){
                if(v < 2) continue;
                res += v * (v-1) / 2;
            }
        }
        return res*2;
    }
}