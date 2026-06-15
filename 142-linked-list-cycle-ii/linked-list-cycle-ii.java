/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null ||head.next==null){
            return null;
        }
        ListNode sl=head;
        ListNode ft=head;
        while(ft.next!=null && ft.next.next!=null){
            sl=sl.next;
            ft=ft.next.next;
            if(sl==ft){
                ListNode st=head;
                while(st!=sl){
                    sl=sl.next;
                    st=st.next;
                }
                return st;
            }
        }

            
        return null;
    }
}
      