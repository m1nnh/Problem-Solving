/*
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 정수 1개 입력받아 나누어 출력하기
description : 기초 - 입출력
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class CodeUp_1025 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        for (int i = 0; i < s.length(); i++)
            System.out.println(s.charAt(i));
    }
}
