import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt(); 

        for (int test = 0; test < t; test++) {
            int n = sc.nextInt();
            int[] a = new int[n];


            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }

            if (solve(a, n)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }


    public static boolean solve(int[] a, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j < n; j++) {
                if (a[i] == a[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
