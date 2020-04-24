class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> st = new Stack<>();
        for(int i : asteroids){
            if(st.isEmpty()) st.push(i);
            else{
                if(st.peek() < 0 && i > 0) st.push(i);
                else if(i < 0 && st.peek() > 0){
                    int n = i;
                    while(!st.isEmpty() && st.peek() > 0 && n < 0){
                        if(n + st.peek() == 0){n = 0; st.pop();}
                        else{
                            n = Math.abs(n) > Math.abs(st.peek())? n : st.peek();
                            st.pop();
                        }
                    }
                    if(n != 0) st.push(n);
                }else{
                    st.push(i);
                }
            }
        }
        int[] res = new int[st.size()];
        int id = res.length-1;
        while(!st.isEmpty()) res[id--] = st.pop();
        return res;
    }
    /*
    private boolean diff(int a, int b){
        if(a > 0 && b < 0) return true;
        if(a < 0 && b > 0) return true;
        return false;
    }
    */
}