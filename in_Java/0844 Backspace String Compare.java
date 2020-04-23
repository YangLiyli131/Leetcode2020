class Solution {
    public boolean backspaceCompare(String S, String T) {
        Stack<Character> st1 = new Stack<>();
        Stack<Character> st2 = new Stack<>();
        for(char c : S.toCharArray()){
            if(c == '#'){
                if(!st1.isEmpty()) st1.pop();
            }else{
                st1.push(c);
            }
        }
        for(char c : T.toCharArray()){
            if(c == '#'){
                if(!st2.isEmpty()) st2.pop();
            }else{
                st2.push(c);
            }
        }
        if(st1.size() != st2.size()) return false;
        while(!st1.isEmpty()){
            if(st1.pop() != st2.pop()) return false;
        }
        return true;
    }
}