package sliding_window;

import java.util.HashSet;

public class S3 {
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            HashSet<Character> set = new HashSet<>();
            int left = 0;
            int right = 0;
            int ans = 0;
            while (right < s.length()) {
                char cur = s.charAt(right);
                while (set.contains(cur)) {
                    set.remove(s.charAt(left));
                    left++;
                }
                set.add(s.charAt(right));
                ans = Math.max(ans, right - left + 1);
                right++;
            }
            return ans;
        }
    }
}
