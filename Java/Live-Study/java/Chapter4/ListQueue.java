package Chapter4;

public class ListQueue {
    private ListNode node = null;

    private ListNode head;

    public ListQueue() {
    }

    public ListQueue(int element) {
        node = new ListNode(element);
        head = node;
    }

    public void offer(int data) {
        if (node == null) {
            node = new ListNode(data);
            head = node;
        } else {
            ListNode nextNode = node;
            while (nextNode.next != null) {
                nextNode = nextNode.next;
            }
            nextNode.next = new ListNode(data);
        }
    }

    public int poll() {
        int result = head.elements;

        ListNode nextNode = head.next;
        head = null;
        head = nextNode;

        return result;
    }

    public int size() {
        int size = 0;
        ListNode nextNode = head;
        while (nextNode != null) {
            ++size;
            nextNode = nextNode.next;
        }
        return size;
    }

    public void print() {
        if (head == null) {
            System.out.println("is empty");
        } else if (head.next == null) {
            System.out.println(node.elements);
        } else {
            ListNode nextNode = head;
            while (nextNode != null) {
                System.out.println(nextNode.elements);
                nextNode = nextNode.next;
            }
        }


    }

    public static class ListNode {
        private int elements;
        private ListNode next = null;

        public ListNode(int data) {
            elements = data;
        }
    }
}
