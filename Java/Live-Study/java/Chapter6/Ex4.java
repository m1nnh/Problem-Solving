package Chapter6;

public class Ex4 {
    static double getDistance(int x, int y, int x1, int y1) {
        return Math.sqrt(Math.abs(x1 - x) + Math.abs(y1 - y));
    }

    public static void main(String[] args) {
        System.out.println(getDistance(1, 1, 2, 2));
    }
}
