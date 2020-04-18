class Solution {
    public int[] shortestToChar(String S, char C) {
        int[] res = new int[S.length()];
        List<Integer> L = new ArrayList<>();
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == C) L.add(i);
        }
        for(int i = 0; i < S.length();i++){
            int cur = Integer.MAX_VALUE;
            for(int x : L){
                if(Math.abs(x-i) < cur) cur = Math.abs(x-i);
            }
            res[i] = cur;
        }
        return res;
    }
}