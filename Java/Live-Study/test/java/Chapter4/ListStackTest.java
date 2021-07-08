package Chapter4;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class ListStackTest {

    @Test
    @DisplayName("listNodeStack Test")
    void pushStackTest() {
        ListStack stack = new ListStack();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());

        stack.push(100);
        stack.print();
        System.out.println(stack.pop());
        stack.print();
    }

}