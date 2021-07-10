package Chapter6;

class MyTv {
    boolean isPowerOn;
    int channel;
    int volume;

    final int MAX_VOLUME = 100;
    final int MIN_VOLUIME = 0;
    final int MAX_CHANNEL = 100;
    final int MIN_CHANNEL = 1;

    void turnOnOff() {
        if (isPowerOn) {
            isPowerOn = false;
        } else {
            isPowerOn = true;
        }
    }

    void volumeUp() {
        if (volume < MAX_VOLUME) {
            volume += 1;
        }
    }

    void volumeDown() {
        if (volume > MIN_VOLUIME) {
            volume -= 1;
        }
    }

    void channelUp() {
        if (channel < MAX_CHANNEL) {
            channel += 1;
        } else {
            channel = MIN_CHANNEL;
        }
    }

    void channelDown() {
        if (channel > MIN_CHANNEL) {
            channel -= 1;
        } else {
            channel = MAX_CHANNEL;
        }
    }
}

public class Ex6 {
    public static void main(String[] args) {
        MyTv t = new MyTv();
        t.channel = 100;
        t.volume = 0;
        System.out.println("CH:" + t.channel + ", VOL:" + t.volume);
        t.channelDown();
        t.volumeDown();
        System.out.println("CH:" + t.channel + ", VOL:" + t.volume);
        t.volume = 100;
        t.channelUp();
        t.volumeUp();
        System.out.println("CH:" + t.channel + ", VOL:" + t.volume);
    }
}
