/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null) return root;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        Node cur;
        Node pre;
        int n;
        while(!q.isEmpty()){
            n = q.size();
            pre = q.poll();
            if(pre.left != null) q.add(pre.left);
            if(pre.right != null) q.add(pre.right);
            n--;
            while(n-- != 0){
                cur = q.poll();
                pre.next = cur;
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
                pre = cur;
            }
            pre.next = null;
        }
        return root;
    }
}