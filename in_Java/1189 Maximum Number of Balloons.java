class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character,Integer> hm = new HashMap<>();
        for(char c : text.toCharArray()){
            if(c == 'b' || c == 'a' || c == 'l' || c == 'o' || c == 'n'){
                if(!hm.containsKey(c)) hm.put(c,1);
                else hm.put(c, hm.get(c)+1);
            }
        }
        if(hm.keySet().size() < 5) return 0;
        int a = Math.min(hm.get('n'),Math.min(hm.get('b'), hm.get('a')));
        int b = Math.min(hm.get('l'), hm.get('o'));
        return Math.min(a, b/2);
    }
}