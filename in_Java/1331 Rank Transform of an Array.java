class Solution {
    public int[] arrayRankTransform(int[] arr) {
        Set<Integer> hs = new HashSet<>();
        for(int i : arr) hs.add(i);
        int[] t = new int[hs.size()];
        int id = 0;
        for(int i : hs) t[id++] = i;
        Arrays.sort(t);
        int[] res = new int[arr.length];
        for(int i = 0; i < res.length; i++){
            res[i] = ido(t,arr[i]) + 1;
        }
        return res;
    }
    private int ido(int[] n, int x){
        int i = 0;
        int j = n.length-1;
        int m;
        while(i <= j){
            m = i + (j-i)/2;
            if(n[m] == x){
                return m;
            }else if(n[m] > x){
                j = m-1;
            }else{
                i = m+1;
            }
        }
        return -1;
    }
}