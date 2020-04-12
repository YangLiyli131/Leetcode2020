class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int l = p.length();
        char[] ch = p.toCharArray();
        Arrays.sort(ch);
        String tar = String.valueOf(ch);
        List<Integer> res = new ArrayList<>();
        String t;
        String tt;
        char[] chh;
        for(int i = 0; i <= s.length()-l; i++){
            t = s.substring(i,i+l);
            chh = t.toCharArray();
            Arrays.sort(chh);
            tt = String.valueOf(chh);
            if(tt.equals(tar)) res.add(i);
        }
        return res;
    }
}