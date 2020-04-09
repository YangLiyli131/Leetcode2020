class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        List<String> res = new ArrayList<>();
        String[] ss = text.split(" ");
        for(int i = 0; i < ss.length-2; i++){
            if(ss[i].equals(first) && ss[i+1].equals(second)) res.add(ss[i+2]);
        }
        String[] x = new String[res.size()];
        for(int i = 0; i < x.length; i++) x[i] = res.get(i);
        return x;
    }
}