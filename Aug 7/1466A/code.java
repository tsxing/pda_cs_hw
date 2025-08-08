import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t= sc.nextInt();
        
        for (int test=0; test<t; test++){
            int n = sc.nextInt();
            int[] a = new int[n];
            
            for (int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            
            System.out.println(solve(a));
        }
        
        sc.close();
    }
    
    public static int solve(int[] a){
        Set<Integer> differences = new HashSet<>();
        
        for (int i=0; i<a.length; i++){
            for (int j=i+1; j<a.length; j++){
                differences.add(a[i] - a[j]);
            }
        }
        
        return differences.size();
    }
}
