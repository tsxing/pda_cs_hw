import java.io.*;
import java.util.*;

class Main {
    static int N;
    static int[] bales;

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new FileReader("angry.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("angry.out")));

        N = Integer.parseInt(r.readLine());
        bales = new int[N];
        for (int i = 0; i < N; i++) {
            bales[i] = Integer.parseInt(r.readLine());
        }
        Arrays.sort(bales);

        int ans = 1;
        for (int i = 0; i < N; i++) {
            int r_amt = right_most(i);
            int l_amt = left_most(i);
            int exploded = r_amt - l_amt + 1;
            if (exploded > ans) {
                ans = exploded;
            }
        }

        pw.println(ans);
        pw.close();
        r.close();
    }

    public static int right_most(int start) {
        int last = start;
        int rad = 1;
        while (true) {
            int neww = last;
            while ((0 <= neww + 1 && neww + 1 < N) && (Math.abs(bales[neww + 1] - bales[last]) <= rad)) {
                neww++;
            }
            if (neww == last) {
                break;
            }
            last = neww;
            rad++;
        }
        return last;
    }

    public static int left_most(int start) {
        int last = start;
        int rad = 1;
        while (true) {
            int neww = last;
            while ((0 <= neww - 1 && neww - 1 < N) && (Math.abs(bales[neww - 1] - bales[last]) <= rad)) {
                neww--;
            }
            if (neww == last) {
                break;
            }
            last = neww;
            rad++;
        }
        return last;
    }
}
