package Chapter4;

public class Ex1 {
    public static void main(String[] args) {
        int odd_sum = 0;
        int even_sum = 0;
        for (int i = 1; i <= 20; i++) {
            if (i % 2 == 0)
                even_sum += i;
            else
                odd_sum += i;
        }

        System.out.printf("홀수의 합 : %d%n짝수의 합 : %d%n", odd_sum, even_sum);

    }

    public int oddTest() {
        int odd_sum = 0;
        int even_sum = 0;
        for (int i = 1; i <= 20; i++) {
            if (i % 2 == 0)
                even_sum += i;
            else
                odd_sum += i;
        }

        return odd_sum;

    }

    public int evenTest() {
        int odd_sum = 0;
        int even_sum = 0;
        for (int i = 1; i <= 20; i++) {
            if (i % 2 == 0)
                even_sum += i;
            else
                odd_sum += i;
        }

        return even_sum;

    }
}
