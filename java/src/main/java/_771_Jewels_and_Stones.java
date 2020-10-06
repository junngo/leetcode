import java.util.HashMap;
import java.util.Map;

public class _771_Jewels_and_Stones {
    public int numJewelsInStones(String J, String S) {
        Map<String, Integer> map = new HashMap<>();
        String word = "";
        int cnt = 0;

        for(int i = 0; i < S.length(); i++) {
            word = String.valueOf(S.charAt(i));
            if (map.containsKey(word)) {
                cnt = map.get(word) + 1;
            } else {
                cnt = 1;
            }
            map.put(word, cnt);
        }

        cnt = 0;
        for (int i = 0; i < J.length(); i++) {
            word = String.valueOf(J.charAt(i));
            if (map.containsKey(word)) {
                cnt += map.get(word);
            }
        }

        return cnt;
    }

    public static void main(String[] args) {
        int ret = new _771_Jewels_and_Stones().numJewelsInStones("aA", "aAAbbbb");
        System.out.println(ret);
    }
}
