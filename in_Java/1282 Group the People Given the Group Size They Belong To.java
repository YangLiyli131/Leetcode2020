class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> res = new ArrayList<>();
        if(groupSizes == null || groupSizes.length == 0) return res;
        HashMap<Integer,List<Integer>> hm = new HashMap<>();
        List<Integer> cur;
        for(int i = 0; i < groupSizes.length; i++){
            if(!hm.containsKey(groupSizes[i])){
                cur = new ArrayList<Integer>();
                cur.add(i);
                hm.put(groupSizes[i], cur);
            }else{
                cur = hm.get(groupSizes[i]);
                cur.add(i);
                hm.put(groupSizes[i], cur);
            }
        }
        for(int k : hm.keySet()){
            cur = hm.get(k);
            int len = k;
            while(cur.size() != 0){
                List<Integer> temp = new ArrayList<>();
                while(len-- != 0){                    
                    temp.add(cur.remove(0));
                }
                res.add(temp);
                len = k;
            }            
        }
        return res;
    }
}