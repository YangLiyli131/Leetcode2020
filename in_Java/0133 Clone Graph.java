/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    Map<Integer, Node> hm = new HashMap<>();
    public Node cloneGraph(Node node) {
        return dfs(node);
    }
    private Node dfs(Node n){
        if(n == null) return n;
        if(hm.containsKey(n.val)) return hm.get(n.val);
        Node nn = new Node(n.val, new ArrayList<Node>());
        hm.put(n.val, nn);
        for(Node nei : n.neighbors){
            nn.neighbors.add(dfs(nei));
        }
        return nn;
    }
}