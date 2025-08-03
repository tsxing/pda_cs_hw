import java.io.*;
import java.util.*; //cbarn

public class cbarn {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("cbarn.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cbarn.out")));

        int n = Integer.parseInt(br.readLine());
        int[] log = new int[n];
        for (int i = 0; i < n; i++) {
            log[i] = Integer.parseInt(br.readLine());
        }

        long ans = Long.MAX_VALUE;
        long tot = 0;
        for (int i = 0; i < n; i++) {
            tot += log[i];
        }

        for (int start_door = 0; start_door < n; start_door++) {
            long dist = 0;
            long remaining = tot;
            for (int r = 0; r < n; r++) {
                remaining -= log[(start_door + r) % n];
                dist += remaining;
            }
            ans = Math.min(ans, dist);
        }

        pw.println(ans);
        pw.close();
        br.close();
    }
}
