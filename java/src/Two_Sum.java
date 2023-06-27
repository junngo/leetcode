import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Two_Sum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int value = target - nums[i];
            if (numMap.containsKey(value)) {
                return new int[] {numMap.get(value), i};
            }
            numMap.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = new Two_Sum().twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }
}
