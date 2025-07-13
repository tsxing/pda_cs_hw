import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        
        for (int test=0;test<t;test++){
            int x1 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y2 = scanner.nextInt();

            if (x1 == x2) {
                System.out.println(Math.abs(y2 - y1));
            } else if (y1 == y2) {
                System.out.println(Math.abs(x2 - x1));
            } else {
                System.out.println(Math.abs(y2 - y1) + Math.abs(x2 - x1) + 2);
            }
        }

    }
}
