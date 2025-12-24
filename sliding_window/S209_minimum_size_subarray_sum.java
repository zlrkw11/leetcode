package sliding_window;

public class S209_minimum_size_subarray_sum {
    class Solution {
        public int minSubArrayLen(int target, int[] nums) {
            int left = 0;
            int right = 0;
            int sum = 0;
            int minLen = Integer.MAX_VALUE;

            while (right < nums.length) {
                sum += nums[right];
                right++;
                while (sum >= target) {
                    minLen = Math.min(minLen, right - left);
                    sum -= nums[left];
                    left++;
                }
            }
            if (minLen == Integer.MAX_VALUE) {
                return 0;
            }
            return minLen;
        }
    }
}
