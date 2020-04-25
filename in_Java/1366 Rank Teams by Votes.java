class Solution {
    public String rankTeams(String[] votes) {
        int nt = votes[0].length();
        Map<Character,int[]> hm = new HashMap<>();
        for(String s : votes){
            for(int i = 0; i < nt; i++){
                char c = s.charAt(i);
                hm.putIfAbsent(c, new int[nt]);
                hm.get(c)[i]++;
            }
        }
        List<Character> L = new ArrayList<>(hm.keySet());
        Collections.sort(L,(a,b)->{
            for(int i = 0; i < nt; i++){
                if(hm.get(a)[i] != hm.get(b)[i]){
                    return hm.get(b)[i] - hm.get(a)[i];
                }
            }
            return a-b;
        });
        StringBuilder sb = new StringBuilder();
        for(char c : L) sb.append(c);
        return sb.toString();
    }
}