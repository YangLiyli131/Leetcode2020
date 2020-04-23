class MyStack {
    Queue<Integer> q;
    int n;
    /** Initialize your data structure here. */
    public MyStack() {
        q = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        q.add(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        n = q.size();
        while(n-- != 1){
            q.add(q.poll());
        }
        return q.poll();
    }
    
    /** Get the top element. */
    public int top() {
        n = q.size();
        while(n-- != 1){
            q.add(q.poll());
        }
        int res = q.poll();
        q.add(res);
        return res;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */