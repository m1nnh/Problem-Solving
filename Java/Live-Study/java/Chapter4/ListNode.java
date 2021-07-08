package Chapter4;

import lombok.Data;

@Data
public class ListNode {
    public int elements;
    public ListNode next = null;

    public ListNode(int data) {
        elements = data;
    }

    public ListNode add(ListNode newElement) {
        if (this.next == null) {
            this.next = newElement;
            return this;
        }

        ListNode nextNode = this.next;
        while (nextNode.next != null)
            nextNode = nextNode.next;

        nextNode.next = newElement;

        return this;
    }

    public ListNode add(ListNode head, ListNode nodeToAdd, int position) {
        ListNode nextNode = head;

        for (int loop = 0; loop < position - 1; loop++) {
            if (nextNode.next == null)
                break;
            nextNode = nextNode.next;
        }

        ListNode tmp = nextNode.next;
        nextNode.next = nodeToAdd;
        nodeToAdd.next = tmp;

        return this;
    }

    public ListNode remove(ListNode head, int positionToRemove) {
        ListNode nextNode = head;

        for (int loop = 0; loop < positionToRemove - 1; loop++)
            nextNode = nextNode.next;

        ListNode tmp = nextNode.next;
        nextNode.next = tmp.next;
        tmp = null;

        return this;
    }

    public boolean contains(ListNode head, ListNode nodeToCheck) {
        ListNode nextNode = head;

        while (nextNode.next != null) {
            if (nextNode.elements == nodeToCheck.elements)
                return true;
            nextNode = nextNode.next;
        }
        return false;
    }

    public void printForEach() {
        ListNode nextNode = this;

        while (nextNode != null) {
            System.out.println(nextNode.elements);
            nextNode = nextNode.next;
        }
    }

    public int size() {
        ListNode nextNode = this;
        int size = 0;

        while (nextNode != null) {
            ++size;
            nextNode = nextNode.next;
        }

        return size;

    }
}
