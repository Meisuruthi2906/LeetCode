class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy=new ListNode(0);// create dummy Node
        dummy.next=head;           
        ListNode grpTail=dummy;       //cerate dummy node cnt with grpTail
        while(head!=null){                      //if head!=null move that in next
            ListNode temp=head;                    //temp node create in head node
            for(int i=0;i<k;i++){
                //temp=temp.next;                
                if(temp==null) return dummy.next;
                temp=temp.next; //if temp node ==null return for the origina node 
            }
            ListNode prev=null;
            // ListNode next=null;
            ListNode curr=head;             //three pointer creatr for the k group in reverse concpr because their are sll
            for(int i=0;i<k;i++){ 
                ListNode next=curr.next;
                              //initial =0 end=less than k
                curr.next=prev;
                prev=curr;
                curr=next;
            }
            grpTail.next=prev;
            head.next=curr;
            grpTail=head;
            head=curr;
        }
        return dummy.next;
    }
}

