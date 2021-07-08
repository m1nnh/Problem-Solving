package Chapter3;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class OperatorEx9Test {
    OperatorEx9 operatorEx9 = new OperatorEx9();

    @Test
    void test() {
        int a =  operatorEx9.main();
        System.out.println(a);

        Assertions.assertEquals(10000, a);
    }
}