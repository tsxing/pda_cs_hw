import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] p = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = sc.nextInt();
        }

        int cnt = 0;

        for (int i = 0; i < N; i++) {
            int total = 0;
            for (int j = i; j < N; j++) {
                total += p[j];
                int length = j - i + 1;

                if (total % length != 0) {
                    continue;
                }

                int avg = total / length;

                for (int k = i; k <= j; k++) {
                    if (p[k] == avg) {
                        cnt++;
                        break;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}
