class Solution {
    public int[] gardenNoAdj(int N, int[][] paths) {
        Map<Integer, Set<Integer>> hm = new HashMap<>();
        for(int i = 1; i <= N; i++) hm.put(i, new HashSet<Integer>());
        for(int[] p : paths){
            hm.get(p[0]).add(p[1]);
            hm.get(p[1]).add(p[0]);
        }
        int[] res = new int[N];
        for(int i = 1; i <= N; i++){
            int[] colors = new int[5];
            for(int j : hm.get(i)){
                colors[res[j-1]] = 1;
            }
            for(int id = 0; id < 5; id++){
                if(colors[id] == 0) res[i-1] = id;
            }
        }
        return res;
    }
}