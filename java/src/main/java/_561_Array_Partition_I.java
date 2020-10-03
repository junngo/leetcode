import java.util.Arrays;

public class _561_Array_Partition_I {
    public static int arrayPairSum(int[] nums) {
        int sum = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                sum += nums[i];
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int ret = arrayPairSum(new int[] {1, 4, 3, 2});
        System.out.println(ret);
    }
}
