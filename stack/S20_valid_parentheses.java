package stack;

import java.util.Stack;
import java.util.HashMap;

public class S20_valid_parentheses {

    class Solution {
        public boolean isValid(String s) {
            HashMap<Character, Character> map = new HashMap<>();
            Stack<Character> stk = new Stack<>();
            map.put(')', '(');
            map.put(']', '[');
            map.put('}', '{');

            for (int i = 0; i < s.length(); i++) {
                if (map.containsKey(s.charAt(i))) {
                    if (stk.isEmpty() || stk.pop() != map.get(s.charAt(i))) {
                        return false;
                    }
                } else {
                    stk.push(s.charAt(i));
                }

            }
            if (stk.isEmpty()) {
                return true;
            }
            return false;
        }
    }
}
