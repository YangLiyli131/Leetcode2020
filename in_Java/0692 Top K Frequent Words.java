class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> hm = new HashMap<>();
        for(String s : words) hm.put(s, hm.getOrDefault(s,0)+1);
        PriorityQueue<Map.Entry<String,Integer>> pq = new PriorityQueue<>((i,j) -> i.getValue() == j.getValue()? i.getKey().compareTo(j.getKey()) : j.getValue() - i.getValue());
        pq.addAll(hm.entrySet());
        List<String> res = new ArrayList<>();
        while(k-- != 0) res.add(pq.poll().getKey());
        return res;
    }
}

