package Chapter4;

public class Ex2 {
    public static void main(String[] args) {
        int sumValue = 0;
        for (int i = 1; i <= 10; i++) {
            for (int j = 1; j <= i; j++)
                sumValue += j;
        }

        System.out.println(sumValue);
    }

    public int sumTest() {
        int sumValue = 0;
        for (int i = 1; i <= 10; i++) {
            for (int j = 1; j <= i; j++)
                sumValue += j;
        }

        return sumValue;
    }
}

