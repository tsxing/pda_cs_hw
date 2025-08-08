import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            
            if (d >= b && (d - b) >= (c - a)) {
                System.out.println((d - b) + (a + d - b - c));
            } else {
                System.out.println(-1);
            }
        }
        
        sc.close();
    }
}
