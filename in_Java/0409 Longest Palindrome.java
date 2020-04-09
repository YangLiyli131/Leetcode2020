class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character,Integer> hm = new HashMap<>();
        for(char c : s.toCharArray()){
            if(!hm.containsKey(c)){
                hm.put(c,1);
            }else{
                hm.put(c,hm.get(c)+1);
            }
        }
        int res = 0;
        boolean flag = false;
        for(int i : hm.values()){
            if(i % 2 == 0) res += i;
            else{
                flag = true;
                res += i-1;
            }            
        }
        return flag? res+1 : res;
    }
}