package Chapter4;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class ListNodeTest {
    @Test
    @DisplayName("LinkedList forEachTest")
    void nodePrintForEach(){

        ListNode list = new ListNode(10);
        list.add(new ListNode(20));
        list.add(new ListNode(30));
        list.add(new ListNode(40));
        list.add(new ListNode(50));


        list.printForEach();

    }

    @Test
    @DisplayName("LinkedList containsTest")
    void nodeContainsTest(){

        ListNode node = new ListNode(10);
        node.add(new ListNode(20));
        node.add(new ListNode(30));
        node.add(new ListNode(40));
        node.add(new ListNode(50));

        System.out.println(node.contains(node, new ListNode(50))); // true
        System.out.println(node.contains(node, new ListNode(30))); // true
        System.out.println(node.contains(node, new ListNode(60))); // false
        System.out.println(node.contains(node, node));

    }

    @Test
    @DisplayName("LinkedList addTest")
    void nodeAddTest(){

        ListNode node = new ListNode(10);
        node.add(new ListNode(20));
        node.add(new ListNode(30));
        node.add(new ListNode(40));
        node.add(new ListNode(50));

        node.add(node, new ListNode(100), 3);

        node.printForEach();

    }

    @Test
    @DisplayName("LinkedList removeTest")
    void nodeRemoveTest(){

        ListNode node = new ListNode(10);
        node.add(new ListNode(20));
        node.add(new ListNode(30));
        node.add(new ListNode(40));
        node.add(new ListNode(50));

        node.remove(node, 3);

        node.printForEach();

    }

    @Test
    @DisplayName("LinkedList sizeTest")
    void nodeSizeTest(){

        ListNode node = new ListNode(10);
        node.add(new ListNode(20));
        node.add(new ListNode(30));
        node.add(new ListNode(40));
        node.add(new ListNode(50));

        System.out.println(node.size());

    }

}