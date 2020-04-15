class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        HashMap<int[], Integer> hm = new HashMap<>();
        boolean f;
        for(int i = 0; i < dominoes.length; i++){
            f = false;
            int[] cur = dominoes[i];
            Arrays.sort(cur);
            for(int[] k : hm.keySet()){
                if(k[0] == cur[0] && k[1] == cur[1]){
                    hm.put(k, hm.get(k)+1);
                    f = true;
                }
            }
            if(!f) hm.put(cur,1);
        }
        int res = 0;
        for(int i : hm.values()){
            //System.out.println(i);
            if(i > 1){
                res += i * (i-1)/2;
            }
        }
        return res;
    }
}