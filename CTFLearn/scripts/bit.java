public class bit {
    public static void main(String[] args) {
        int a = 525024598;
        int b = -889275714;

        for (int i = Integer.MIN_VALUE; i < Integer.MAX_VALUE; i++) {
            int s1 = (i << 3) ^ (a ^ i);
            if (s1 == b) {
                System.out.println("Proper input: " + i);
                break;
            }
        }

    }
}
