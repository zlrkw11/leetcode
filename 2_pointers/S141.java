import java.util.HashMap;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class S141 {
    public class Solution {
        public boolean hasCycle(ListNode head) {
            HashMap<ListNode, Number> map = new HashMap<>();
            ListNode curr = head;
            while (curr.next != null) {

            }

            return true;
        }
    }
}
