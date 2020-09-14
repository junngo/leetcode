public class _004_Median_of_Two_Sorted_Arrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        for (int i = 0; i < nums1.length; i++) {
            System.out.println(nums1[i]);
        }

        return 0.0;
    }

    public static void main(String[] args) {
        double ret = new _004_Median_of_Two_Sorted_Arrays().findMedianSortedArrays(
                new int[] {1, 2, 3}, new int[] {2}
        );
    }
}
