package Chapter6;

public class Ex1 {
    public static void main(String[] args) {
        StudaCard card1 = new StudaCard(3, false);
        StudaCard card2 = new StudaCard();

        System.out.println(card1.info());
        System.out.println(card2.info());
    }
}

class StudaCard {
    int num;
    boolean isKwang;

    StudaCard() {
        this.num = 1;
        this.isKwang = true;
    }

    StudaCard(int num, boolean isKwang) {
        this.num = num;
        this.isKwang = isKwang;
    }

    String info() {
        if (isKwang)
           return Integer.toString(num) + "K";
        else
            return Integer.toString(num);
    }
}
