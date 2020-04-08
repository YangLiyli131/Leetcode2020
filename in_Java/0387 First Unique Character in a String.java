class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> hm = new HashMap<>();
        for(char c : s.toCharArray()){
            if(!hm.containsKey(c)){
                hm.put(c,1);
            }else{
                hm.put(c,hm.get(c)+1);
            }
        }
        int res = -1;
        for(int i = 0; i < s.length(); i++){
            if(hm.get(s.charAt(i)) == 1){
                res = i;
                break;
            }
        }
        return res;
    }
}