package Chapter6;

import static java.lang.Math.round;

public class Ex2 {

    public static void main(String[] args) {
        Student s = new Student();
        s.name = "홍길동";
        s.ban = 1;
        s.no = 1;
        s.kor = 100;
        s.eng = 60;
        s.math = 76;

        System.out.println("이름 : " + s.name);
        System.out.println("총점 : " + s.getTotal());
        System.out.println("평균 : " + s.getAverage());
    }
}

class Student {
    String name;
    int ban;
    int no;
    int kor;
    int eng;
    int math;

    Student() {
        this.name = "";
        this.ban = 0;
        this.no = 0;
        this.kor = 0;
        this.eng = 0;
        this.math = 0;
    }

    Student(String name, int ban, int no, int kor, int eng, int math) {
        this.name = name;
        this.ban = ban;
        this.no = no;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    int getTotal() {
        return kor + eng + math;
    }

    float getAverage() {
        return round((float) (kor + eng + math) / 3);
    }

    String info() {
        return name + "," + Integer.toString(ban) + "," + Integer.toString(no) + "," + Integer.toString(kor) + ","
                + Integer.toString(eng) + "," + Integer.toString(math) + "," + Integer.toString(getTotal()) + "," + Float.toString(getAverage());
    }
}