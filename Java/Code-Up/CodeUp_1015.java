/*
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 실수 입력받아 둘째 자리까지 출력하기
description : 기초 - 입출력
*/

public class CodeUp_1015 {
    public static void main(String[] args) {
        double m = 50.349;
        System.out.printf("%.2f", (double) Math.round(m * 100) / 100);
    }
}
