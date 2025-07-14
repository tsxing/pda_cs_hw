import java.io.*;
import java.util.*;
import java.lang.Math;


class Main {
    static int N;
    static int bales[];
    public static void main(String[] args) throws IOException {
	    
	BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
	PrintWriter pw = new PrintWriter(System.out);

        
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); 
        bales = new int[N];
        for (int i = 0; i < N; i++) {
            bales[i] = sc.nextInt();
        }
        Arrays.sort(bales);
        int ans = 1;
        
        for (int i=0;i<N;i++){
            int r = right_most(i);
            int l = left_most(i);
            int exploded = r- l+1;
            if (exploded >ans){
                ans = exploded;
            }
        }
        pw.println(ans);
        pw.close();
        br.close();
        
    }
    
    public static int right_most(int start){
        int last = start;
        int r = 1;
        while (true){
            int neww = last;
            while ((0 <= neww + 1 && neww + 1 < N) && (Math.abs(bales[neww + 1] - bales[last]) <= r)){
                neww++;
                
            }
            if (neww==last){
                break;
            }
            last= neww;
            r++;
        }
        return last;
    }
    
    public static int left_most(int start){
        int last = start;
        int r = 1;
        while (true){
            int neww = last;
            while ((0 <= neww - 1 && neww - 1 < N) && (Math.abs(bales[neww - 1] - bales[last]) <= r)){
                neww--;
                
            }
            if (neww==last){
                break;
            }
            last= neww;
            r++;
        }
        return last;
    }
    
    
}
