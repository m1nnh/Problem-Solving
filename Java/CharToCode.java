/*
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Java Jungsuk Ex 02 - 07
description : Char
*/

package JavaJungsuk;

public class CharToCode {
    public static void main(String[] args) {
        char ch = 'A';
        int code = (int) ch;

        System.out.printf("%c=%d(%#X)%n", ch, code, code);

        char hch = '가';
        System.out.printf("%c=%d(%#X)%n", hch, (int) hch, (int) hch);
    }
}
