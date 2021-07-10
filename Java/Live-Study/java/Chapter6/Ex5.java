package Chapter6;

public class Ex5 {
    public static int[] shuffle(int [] array) {
        for (int i = 0; i < array.length; i++) {
            int num = (int)Math.random() % array.length;
            int temp = array[i];
            array[i] = array[num];
            array[num] = temp;
        }

        return array;
    }

    public static void main(String[] args) {
        int[] original = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(java.util.Arrays.toString(original));

        int[] result = shuffle(original);
        System.out.println(java.util.Arrays.toString(result));
    }
}


