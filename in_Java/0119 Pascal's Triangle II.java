class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> L = new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        //if(rowIndex == 0) return res;
        res.add(1);
        L.add(res);
        if(rowIndex == 0) return res;  
        res = new ArrayList<>();
        res.add(1);
        res.add(1);
        L.add(res);
        List<Integer> pre;
        List<Integer> cur;
        for(int i = 2; i <= rowIndex; i++){
            pre = L.get(i-1);
            cur = new ArrayList<>();
            cur.add(1);
            for(int j = 1; j < i; j++){
                cur.add(pre.get(j)+pre.get(j-1));
            }
            cur.add(1);
            L.add(cur);
        }
        return L.get(L.size()-1);
    }
}