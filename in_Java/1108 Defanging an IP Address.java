class Solution {
    public String defangIPaddr(String address) {
        char[] ch = address.toCharArray();
        List<String> l = new ArrayList<>();
        for(char c : ch){
            l.add(String.valueOf(c));
        }
        for(int i = 0; i < ch.length; i++){
            if(l.get(i).equals(".")) l.set(i,"[.]");
        }
        String res = "";
        for(String x : l) res += x;
        return res;
    }
}