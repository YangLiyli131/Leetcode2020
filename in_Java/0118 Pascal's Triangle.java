class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        if(numRows == 0) return res;
        List<Integer> t = new ArrayList<>();
        t.add(1);
        res.add(t);
        if(numRows == 1) return res;
        t = new ArrayList<>();
        t.add(1); t.add(1);
        res.add(t);
        if(numRows == 2) return res;
        for(int i = 3; i <= numRows; i++){
            t = new ArrayList<>();
            t.add(1);
            for(int id = 1; id < i-1; id++){
                t.add(res.get(i-2).get(id-1) + res.get(i-2).get(id));
            }
            t.add(1);
            res.add(t);
        }
        return res;
    }
}