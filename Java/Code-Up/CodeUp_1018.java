/*
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 시간 입력받아 그대로 출력하기
description : 기초 - 입출력
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class CodeUp_1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int h = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        System.out.printf("%d : %d", h, m);
    }
}
