/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head==null || head.next==null){
            return null;
        }
        ListNode prev=null;
        ListNode sl=head;
        ListNode ft=head;
        while(ft!=null && ft.next!=null){
            prev=sl;
            sl=sl.next;
            ft=ft.next.next;
        }
        prev.next=sl.next;
        return head;
    }
    
}

       