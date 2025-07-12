import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        
        int n = inp.nextInt();
        int m = inp.nextInt();
        
        int cnt = 0;
        
        ArrayList<int[]> log = new ArrayList<>();
        ArrayList<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int l = inp.nextInt();
            int r = inp.nextInt();
            log.add(new int[]{l, r});
        }
        
        for (int i = 1; i <= m; i++) {
            boolean covered = false;
            for (int j = 0; j < n; j++) {
                int[] interval = log.get(j);
                if (interval[0] <= i && i <= interval[1]) {
                    covered = true;
                    break;
                }
            }
            if (!covered) {
                cnt++;
                ans.add(i);
            }
        }
        
        System.out.println(cnt);
        for (int i = 0; i < ans.size(); i++) {
            System.out.print(ans.get(i) + " ");
        }
    }
}
