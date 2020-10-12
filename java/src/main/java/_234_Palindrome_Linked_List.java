import java.util.ArrayList;

public class _234_Palindrome_Linked_List {
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }

        ArrayList<ListNode> list = new ArrayList<>();
        ListNode current = head;

        while (current != null) {
            list.add(current);
            current = current.next;
        }

        for (int i = 0; i < list.size() / 2; i++) {
            if(list.get(i).val != list.get(list.size()-1-i).val)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        ListNode ln = new ListNode(1);
        ln.next = new ListNode(2);
        ln.next.next = new ListNode(2);
        ln.next.next.next = new ListNode(1);
        boolean ret = new _234_Palindrome_Linked_List().isPalindrome(ln);
        System.out.println(ret);
    }
}
