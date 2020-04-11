class Solution {
    public String getHint(String secret, String guess) {
        int a = 0;
        int b = 0;
        List<Integer> t;
        List<Integer> tt;
        Map<Character,List<Integer>> hm1 = new HashMap<>();
        for(int i = 0; i < secret.length(); i++){
            char c = secret.charAt(i);
            if(!hm1.containsKey(c)){
                t = new ArrayList<Integer>();
                t.add(i);
                hm1.put(c,t);
            }else{
                tt = hm1.get(c);
                tt.add(i);
                hm1.put(c, tt);
            }
        }
        Map<Character,List<Integer>> hm2 = new HashMap<>();
        for(int i = 0; i < guess.length(); i++){
            char c = guess.charAt(i);
            if(!hm2.containsKey(c)){
                t = new ArrayList<Integer>();
                t.add(i);
                hm2.put(c,t);
            }else{
                tt = hm2.get(c);
                tt.add(i);
                hm2.put(c, tt);
            }
        }
        List<Integer> x;
        List<Integer> y;
        int cur;
        for(char k : hm2.keySet()){
            cur = 0;
            if(hm1.containsKey(k)){
                x = hm1.get(k);
                y = hm2.get(k);
                for(int f : y){
                    if(x.contains(f)) cur++;
                }
                b += Math.min(x.size(), y.size()) - cur;
            }
            a += cur;
        }
        String res = "";
        return res + a + "A" + b + "B";
    }
}