class Solution {
    public List<String> commonChars(String[] A) {
        List<String> res = new ArrayList<>();
        int[] count = new int[26];
        String x = A[0];
        for(char c : x.toCharArray()){
            count[c - 'a']++;
        }
        for(int i = 1; i < A.length; i++){
            String cur = A[i];
            int[] temp = new int[26];
            for(char c : cur.toCharArray()) temp[c-'a']++;
            for(int p = 0; p < 26; p++){
                count[p] = Math.min(count[p], temp[p]);
            }
        }
        for(int i = 0; i < 26; i++){
            if(count[i] != 0){
                int n = count[i];
                while(n-- != 0){
                    res.add(Character.toString('a' + i));
                }
            }
        }
        return res;
    }
}