import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int test = 0; test < t; test++) {
            long n = sc.nextLong(); 
            if (n <= 6) {
                System.out.println(15);
            } else if (n <= 8) {
                System.out.println(20);
            } else if (n <= 10) {
                System.out.println(25);
            } else {
                System.out.println(((n + 1) / 2) * 5);
            }
        }
    }
}
