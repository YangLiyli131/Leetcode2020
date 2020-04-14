class Solution {
    public int findLucky(int[] arr) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : arr){
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i,hm.get(i)+1);
        }
        int res = Integer.MIN_VALUE;
        for(int k : hm.keySet()){
            if(k == hm.get(k)){
                res = res < k? k : res;
            }
        }
        return res < 0? -1 : res;
    }
}