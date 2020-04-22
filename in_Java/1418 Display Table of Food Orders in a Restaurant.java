class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> hm = new HashMap<>();
        Set<String> allfood = new HashSet<>();
        Set<String> tables = new HashSet<>();
        for(List<String> x : orders){
            String tableid = x.get(1);
            tables.add(tableid);
            String food = x.get(2);
            allfood.add(food);
            List<String> cur;
            if(!hm.containsKey(tableid)){
                cur = new ArrayList<>();
                cur.add(food);
                hm.put(tableid, cur);
            }else{
                cur = hm.get(tableid);
                cur.add(food);
                hm.put(tableid,cur);
            }
        }
        String[] foodnames = new String[allfood.size()];
        int id = 0;
        for(String f : allfood) foodnames[id++] = f;
        Arrays.sort(foodnames);
        int[] tablename = new int[tables.size()];
        id = 0;
        for(String t : tables) tablename[id++] = Integer.parseInt(t);
        Arrays.sort(tablename);
        String[] tablenames = new String[tables.size()];
        id = 0;
        for(int p : tablename) tablenames[id] = String.valueOf(tablename[id++]);
                
        List<String> r1 = new ArrayList<>();
        r1.add("Table");
        for(String ff: foodnames) r1.add(ff);
        res.add(r1);
        
        for(int i = 0; i < tablenames.length; i++){
            r1 = new ArrayList<>();
            String cur_table = tablenames[i];
            r1.add(cur_table);
            int[] count = new int[foodnames.length];           
            for(int j = 0; j < foodnames.length; j++){
                String fs = foodnames[j];
                for(String oo : hm.get(cur_table)){
                    if(oo.equals(fs)) count[j]++;
                }   
            }
            for(int vv : count) r1.add(String.valueOf(vv));
            res.add(r1);
        }
        return res;
    }
}