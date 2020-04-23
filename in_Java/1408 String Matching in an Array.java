class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> res = new ArrayList<>();
        for(int i = 0; i < words.length; i++){
            String cur = words[i];
            for(int j = 0; j < words.length; j++){
                if(j == i) continue;
                String now = words[j];
                if(now.length() < cur.length()) continue;
                if(check(cur,now)){
                    res.add(cur);
                    break;
                }
            }
        }
        return res;
    }
    private boolean check(String a, String b){
        int n = a.length();
        for(int i = 0; i <= b.length() - n; i++){
            if(b.substring(i,i+n).equals(a)) return true;
        }
        return false;
    }
}