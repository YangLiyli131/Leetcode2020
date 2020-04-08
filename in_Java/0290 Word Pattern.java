class Solution {
    public boolean wordPattern(String pattern, String str) {
        char[] ch = pattern.toCharArray();
        String[] st = str.split(" ");
        if(ch.length != st.length) return false;
        HashMap<Character,String> hm = new HashMap<>();
        for(int i = 0; i < ch.length; i++){
            char a = ch[i];
            String b = st[i];
            if(!hm.containsKey(a)){
                if(hm.containsValue(b)) return false;
                else hm.put(a,b);
            }else{
                if(!hm.get(a).equals(b)) return false;
            }
        }
        return true;
    }
}