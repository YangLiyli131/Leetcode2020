/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        HashMap<Integer,Integer> hm1 = new HashMap<>();
        HashMap<Integer,List<Integer>> hm2 = new HashMap<>();
        for(Employee e : employees){
            int k = e.id;
            int v = e.importance;
            List<Integer> L = e.subordinates;
            hm1.put(k,v);
            hm2.put(k,L);
        }
        int res = 0;
        Set<Integer> visited = new HashSet<>();
        visited.add(id);
        Queue<Integer> q = new LinkedList<>();
        q.add(id);
        int n;
        int cur;
        while(q.size() != 0){
            n = q.size();
            while(n-- != 0){
                cur = q.poll();
                res += hm1.get(cur);
                for(int i : hm2.get(cur)){
                    if(!visited.contains(i)){
                        q.add(i);
                        visited.add(i);
                    }
                }
            }
        }
        return res;
    }
}