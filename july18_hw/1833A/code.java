import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        for (int test=0;test<t;test++){
            int n=sc.nextInt();
            String s=sc.next();
            char[] chars=s.toCharArray();
            
            HashSet<String> log = new HashSet<>();
            for (int i=0;i<n-1;i++){
                log.add(""+chars[i]+ chars[i+1]);
                
            }
            System.out.println(log.size());
            
            
        }
        
    }
}
