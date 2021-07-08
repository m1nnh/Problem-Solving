package Chapter4;

public class ListStack {
    private ListNode node = null;
    private ListNode head;

    public void push(int data) {
        if (node == null) {
            node = new ListNode(data);
            head = node;
        } else {
            ListNode nextNode = node.next;
            while (nextNode.next != null) {
                nextNode.next = new ListNode(data);
            }
            nextNode.next = new ListNode(data);
            head = nextNode.next;
        }
    }

    public int pop() {
        ListNode nextNode = node;
        ListNode preNode = head;

        if (node.next == null)
            node = null;

        while (nextNode.next != null) {
            preNode = nextNode;
            nextNode = nextNode.next;
        }

        int result = head.elements;
        head = preNode;
        preNode.next = null;

        return result;

    }

    public void print() {
        if (node == null) {
            System.out.println("is empty");
        } else if (node.next == null) {
            System.out.println(node.elements);
        } else {
            while (node.next != null) {
                System.out.println(node.elements);
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
