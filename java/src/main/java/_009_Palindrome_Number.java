public class _009_Palindrome_Number {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        int head = 0;
        int tail = str.length() - 1;
        char cHead, cTail;

        while (head <= tail) {
            cHead = str.charAt(head);
            cTail = str.charAt(tail);
            if (cHead != cTail) {
                return false;
            }
            head++;
            tail--;
        }

        return true;
    }

    public static void main(String[] args) {
        boolean boo;
        int value = -121;
        boo = new _009_Palindrome_Number().isPalindrome(value);
        System.out.println(boo);
    }
}
