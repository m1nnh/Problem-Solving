package Chapter4;

public class Ex4 {
    public static void main(String[] args) {
        int sumValue = 0;

        for (int i = 1; i <= 6; i++) {
            for (int j = 1; j <= 6; j++) {
                if (i + j == 6) {
                    sumValue += 1;
                    break;
                }
            }
        }

        System.out.println(sumValue);
    }

    public int sumValueTest() {
        int sumValue = 0;

        for (int i = 1; i <= 6; i++) {
            for (int j = 1; j <= 6; j++) {
                if (i + j == 6) {
                    sumValue += 1;
                    break;
                }
            }
        }

        return sumValue;
    }
}
