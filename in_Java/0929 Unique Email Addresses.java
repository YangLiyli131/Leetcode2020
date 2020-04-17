class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> hs = new HashSet<>();
        for(String s : emails){
            String[] ss = s.split("@");
            String name = ss[0];
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < name.length(); i++){
                String t = name.substring(i,i+1);
                if(t.equals("+")) break;
                if(!t.equals(".")) sb.append(t);
            }
            name = sb.toString();
            hs.add(name + "@" + ss[1]);
        }
        return hs.size();
    }
}