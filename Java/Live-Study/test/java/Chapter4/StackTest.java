package Chapter4;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class StackTest {
    @Test
    @DisplayName("arrayStack Test")
    void stackTest(){
        Stack stack = new Stack();

        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);
        stack.push(60);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());

        stack.push(70);
        System.out.println(stack.pop());

        stack.print();
    }
}