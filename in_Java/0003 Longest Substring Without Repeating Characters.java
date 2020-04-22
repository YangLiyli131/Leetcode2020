class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> hm = new HashMap<>();
        int begin = 0, end = 0, counter = 0, d = 0;
        while(end < s.length()){
            char c = s.charAt(end);
            hm.put(c, hm.getOrDefault(c,0)+1);
            if(hm.get(c) > 1) counter++;
            end++;
            
            while(counter != 0){
                char temp = s.charAt(begin);
                if(hm.get(temp) > 1) counter--;
                hm.put(temp, hm.get(temp)-1);
                begin++;
            }
            d = Math.max(d, end - begin);
        }
        return d;
    }
}