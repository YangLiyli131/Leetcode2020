class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] code = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        HashSet<String> hs = new HashSet<>();
        for(String s : words){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < s.length(); i++){
                sb.append(code[s.charAt(i) - 'a']);
            }
            hs.add(sb.toString());
        }
        return hs.size();
    }
}