package Chapter4;


public class Ex3 {
    public static void main(String[] args) {
        int count = 0;
        int sumValue = 0;
        int i = 1;
        while (sumValue < 100) {
            sumValue += i;
            if (count % 2 == 0)
                i = Math.abs(i) + 1;
            else
                i = (Math.abs(i) + 1) * (-1);
            count += 1;

        }

        System.out.println(count);
    }

    public int countTest() {
        int count = 0;
        int sumValue = 0;
        int i = 1;
        while (sumValue < 100) {
            sumValue += i;
            if (count % 2 == 0)
                i = Math.abs(i) + 1;
            else
                i = (Math.abs(i) + 1) * (-1);
            count += 1;

        }

        return count;
    }
}
