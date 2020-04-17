class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        List<String> res = new ArrayList<>();
        if(cpdomains == null || cpdomains.length == 0) return res;
        HashMap<String, Integer> hm = new HashMap<>();
        for(String s : cpdomains){
            String[] ss = s.split(" ");
            String x = ss[1];
            int a = Integer.parseInt(ss[0]);
            List<Integer> t = new ArrayList<>();
            t.add(-1);
            for(int i = 0; i < x.length(); i++){
                if(x.charAt(i) == '.') t.add(i);
            }
            for(int i : t){
                String cur = x.substring(i+1, x.length());
                if(!hm.containsKey(cur)) hm.put(cur, a);
                else hm.put(cur, hm.get(cur)+a);
            }
        }
        for(String k : hm.keySet()){
            res.add(hm.get(k) + " " + k);
        }
        return res;
    }
}