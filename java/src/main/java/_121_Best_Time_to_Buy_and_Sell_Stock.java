public class _121_Best_Time_to_Buy_and_Sell_Stock {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int min = prices[0], result = 0;
        for (int i : prices) {
            if (i < min) {
                min = i;
            }

            if (result < i - min) {
                result = i - min;
            }
        }

        return result;
    }

    public static void main(String[] args) {
//        int[] arr = {7, 1, 5, 3, 6, 4};
        int[] arr = {7, 6, 4, 3, 1};
        int ret = new _121_Best_Time_to_Buy_and_Sell_Stock().maxProfit(arr);
        System.out.println(ret);
    }
}
