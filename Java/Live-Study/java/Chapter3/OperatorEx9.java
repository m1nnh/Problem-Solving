package Chapter3;

public class OperatorEx9 {
    public int main() {
        int a = 1_000_000;
        int b = 2_000_000;

        long c = a * b;

        long d = 1_000_000 * 1_000_000;
        long e = 1_000_000 * 1_000_000L;

        System.out.println(c);
        System.out.println(d);
        System.out.println(e);

        return a;
    }
}
