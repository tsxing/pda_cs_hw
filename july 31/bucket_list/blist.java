import java.io.*;
import java.util.*;

public class blist {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("blist.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("blist.out")));

        int N = Integer.parseInt(br.readLine());
        int[][] log = new int[N][3];  

        for (int i=0; i< N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            log[i][0]= Integer.parseInt(st.nextToken());
            log[i][1]= Integer.parseInt(st.nextToken()); 
            log[i][2]= Integer.parseInt(st.nextToken()); 
        }

        int ans = 0;
        for (int t=1; t<= 1000; t++) {
            int amt = 0;
            for (int i=0; i< N; i++) {
                if (log[i][0]<= t && t<= log[i][1]) {
                    amt+= log[i][2];
                }
            }
            ans = Math.max(ans, amt);
        }
        pw.println(ans);
        pw.close();
        br.close();
    }
}
