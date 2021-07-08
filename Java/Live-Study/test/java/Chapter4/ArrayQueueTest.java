package Chapter4;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class ArrayQueueTest {
    @Test
    @DisplayName("offer arrayQueue Test")
    void offerArrayQueue() {
        ArrayQueue arrayQueue = new ArrayQueue();
        arrayQueue.offer(10);
        arrayQueue.offer(20);
        arrayQueue.offer(30);
        arrayQueue.offer(40);
        arrayQueue.offer(50);

        System.out.println(arrayQueue.size());

        arrayQueue.print();
    }

    @Test
    @DisplayName("poll arrayQueue Test")
    void pollArrayQueue() {
        ArrayQueue arrayQueue = new ArrayQueue();
        arrayQueue.offer(10);
        arrayQueue.offer(20);
        arrayQueue.offer(30);
        arrayQueue.offer(40);
        arrayQueue.offer(50);

        System.out.println(arrayQueue.poll());
        System.out.println(arrayQueue.poll());
        System.out.println(arrayQueue.poll());
        System.out.println(arrayQueue.poll());
        System.out.println(arrayQueue.poll());

        System.out.println(arrayQueue.size());
    }

}