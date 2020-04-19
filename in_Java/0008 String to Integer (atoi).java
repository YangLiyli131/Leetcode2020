class Solution {
    public int myAtoi(String str) {
        int signed = 1;
        if(str == null || str.length() == 0) return 0;
        char[] ch = str.toCharArray();
        int i = 0; 
        int start;
        while(i < ch.length && ch[i] == ' ') i++;
        if(i == ch.length) return 0;
        if(ch[i] == '+'){
            signed = 1;
            start = i+1;
        }
        else if(ch[i] == '-'){
            signed = -1;
            start = i+1;
        }
        else if(ch[i] < '0' || ch[i] > '9') return 0;
        else start = i;
        
        List<Integer> L = new ArrayList<>();
        while(start < ch.length && ch[start] >= '0' && ch[start] <= '9'){
            L.add(0,ch[start++] - '0');
        }
        int res = 0;
        int id = 0;
        while(id < L.size()){
            if(signed == 1) res += L.get(id) * Math.pow(10, id++);
            else res -= L.get(id) * Math.pow(10, id++);
        }
        return res;
    }
}