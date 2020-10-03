import java.util.ArrayList;
import java.util.List;

public class _004_Median_of_Two_Sorted_Arrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> list = new ArrayList<>();
        for(int i : nums1) {
            list.add(i);
        }
        for(int i : nums2) {
            list.add(i);
        }

        list.sort(null);
        int mid = list.size() / 2;
        if ( list.size() % 2 == 0) {
            return (list.get(mid-1) + list.get(mid)) / 2.0;
        }

        return list.get(mid);
    }

    public static void main(String[] args) {
        double ret = new _004_Median_of_Two_Sorted_Arrays().findMedianSortedArrays(
                new int[] {1, 2}, new int[] {3, 4}
        );
        System.out.println(ret);
    }
}
