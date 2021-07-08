package Chapter4;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class ListQueueTest {
    @Test
    @DisplayName("offer listQueue Test")
    void offerListQueue() {
        ListQueue listQueue = new ListQueue();
        listQueue.offer(10);
        listQueue.offer(20);
        listQueue.offer(30);

        System.out.println(listQueue.size());
    }

    @Test
    @DisplayName("poll listQueue Test")
    void pollListQueue() {
        ListQueue listQueue = new ListQueue();
        listQueue.offer(10);
        listQueue.offer(20);
        listQueue.offer(30);
        listQueue.offer(40);
        listQueue.offer(50);

        listQueue.print();

        System.out.println(listQueue.poll());
        System.out.println(listQueue.poll());
        System.out.println(listQueue.poll());
        System.out.println(listQueue.poll());
        System.out.println(listQueue.poll());

        System.out.println(listQueue.size());

        listQueue.print();
    }

}