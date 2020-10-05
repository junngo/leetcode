public class _206_Reverse_Linked_List {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        return prev;
    }

    public static void main(String[] args) {
        ListNode ln = new ListNode(1);
        ln.next = new ListNode(2);
        ln.next.next = new ListNode(3);
        ln.next.next.next = new ListNode(4);
        ln.next.next.next.next = new ListNode(5);

        ListNode ret = new _206_Reverse_Linked_List().reverseList(ln);
        for(int i = 0; i < 5; i++) {
            System.out.println(ret.val);
            ret = ret.next;
        }
    }
}
