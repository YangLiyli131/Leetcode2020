class Solution {
    public String countAndSay(int n) {
        List<String> arr = new ArrayList<>();
        arr.add("1");
        for(int i = 2; i <= n; i++){
            String pre = arr.get(i-2);
            String cur = "";
            int num = 1;
            int id;
            for(id = 0; id < pre.length(); ){
                if(id < pre.length()-1 && pre.charAt(id+1) == pre.charAt(id)){
                    num++;
                    id++;
                }else{
                    cur += Integer.toString(num);
                    cur += Character.toString(pre.charAt(id));
                    num = 1;
                    id++;
                }
            }
            arr.add(cur);
        }
        return arr.get(n-1);
    }
}