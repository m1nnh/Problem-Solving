package Chapter4;

public class ArrayQueue {
    private int[] elements;
    private int size = 16;
    private final int head = 0;
    private int modifyCount = 0;

    public ArrayQueue() {
        elements = new int[size];
    }

    public ArrayQueue(int size) {
        elements = new int[size];
    }

    public boolean offer(int data) {
        if (modifyCount >= size) {
            return false;
        }
        if (data < 0) {
            return false;
        }

        elements[modifyCount] = data;
        ++modifyCount;
        return true;
    }

    public int poll() {
        int res = elements[head];
        int modify = 0;
        for (int loop = 1; loop < modifyCount; loop++) {
            elements[loop - 1] = elements[loop];
            modify = loop;
        }
        elements[modify] = -1;
        modifyCount = modify;
        return res;
    }

    public int size() {
        int size = 0;
        for (int index : elements) {
            if (index == -1) {
                break;
            }
            if (index == 0) {
                break;
            }
            ++size;
        }
        return size;
    }

    public void print() {
        for (int index : elements) {
            if (index == -1) {
                break;
            }
            if (index == 0) {
                break;
            }
            System.out.println(index);
        }
    }
}
