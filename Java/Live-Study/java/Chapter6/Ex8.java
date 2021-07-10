package Chapter6;

import java.util.Arrays;

public class Ex8 {
    public static int max(int[] arr) {
        if (arr.length == 0 || arr == null) {
            return -9999999;
        } else {
            return Arrays.stream(arr).max().getAsInt();
        }
    }

    public static void main(String[] args) {
        int[] data = {3, 2, 9, 4, 7};
        System.out.println(java.util.Arrays.toString(data));
        System.out.println("최대값:" + max(data));
        System.out.println("최대값:" + max(null));
        System.out.println("최대값:" + max(new int[]{})); // 크기가 0인 배열
    }
}
