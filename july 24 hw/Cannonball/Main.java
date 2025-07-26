import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int S = sc.nextInt();
        int[][] log = new int[N][2];

        for (int i = 0; i < N; i++) {
            log[i][0] = sc.nextInt();
            log[i][1] = sc.nextInt();
        }

        boolean[] line = new boolean[N];
        int curr_pos = S - 1;
        int curr_dir = 1;
        int curr_pow = 1;
        int next_pos = curr_pos + curr_dir * curr_pow;

        while (0 <= curr_pos && curr_pos < N && 0 <= next_pos && next_pos < N) {
            if (log[curr_pos][0] == 0) { // jumpad
                curr_pow += log[curr_pos][1];
                curr_dir *= -1;
            } else if (log[curr_pos][0] == 1) { // target
                if (log[curr_pos][1] <= curr_pow && !line[curr_pos]) {
                    line[curr_pos] = true;
                }
            }

            curr_pos += curr_dir * curr_pow;
        }

        int cnt = 0;
        for (boolean hit : line) {
            if (hit) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
