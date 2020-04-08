/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        int leng = 0;
        ListNode d = head;
        while(d != null){
            d = d.next;
            leng++;
        }
        int[] arr = new int[leng];
        int id = 0;
        ListNode dd = head;
        while(dd != null){
            arr[id++] = dd.val;
            dd = dd.next;
        }
        int[] res = new int[leng];
        Stack<Integer> st = new Stack<>();
        for(int i = 0; i < leng; i++){
            if(st.isEmpty() || arr[i] <= arr[st.peek()]){
                st.push(i);
            }else{
                while(!st.isEmpty() && arr[i] > arr[st.peek()]){
                    res[st.peek()] = arr[i];
                    st.pop();
                }
                st.push(i);
            }
        }
        return res;
    }
}