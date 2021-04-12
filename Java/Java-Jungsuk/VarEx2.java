/*
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Java Jungsuk Ex 02 - 02
description : 변수의 교환
*/

package JavaJungsuk;

public class VarEx2 {
    public static void main(String[] args) {
        int x = 10;
        int y = 20;
        int temp = 0;

        System.out.println("x : " + x + " y : " + y);

        temp = x;
        x = y;
        y = temp;

        System.out.println("x : " + x + " y : " + y);
    }
}
