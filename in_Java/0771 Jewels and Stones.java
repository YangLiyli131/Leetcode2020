class Solution {
    public int numJewelsInStones(String J, String S) {
        int res = 0;
        List<Character> l = new ArrayList<>();
        for(char c : J.toCharArray()) l.add(c);
        for(char c : S.toCharArray()){
            if(l.contains(c)) res++;
        }
        return res;
    }
}