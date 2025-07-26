import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int test =0;test<t;test++){
            int n = sc.nextInt();
            sc.nextLine();
            String[] input = sc.nextLine().split(" ");
            int[] a = new int[input.length];
            for (int i = 0; i < input.length; i++) {
                a[i] = Integer.parseInt(input[i]);
                
            }
            
            if (solve(a)){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
        }
        
        
    }
    public static boolean solve(int[] a){
            int n = a.length;
            if (n==1){
                return true;
            }
            for (int start=0;start<n;start++){
                boolean inc = true;
                boolean dec= true;
                
                for (int i=0;i<n-1;i++){
                    int cur =a[(start+i)%n];
                    int nex = a[(start+i+1)%n];
                    
                    if (nex<=cur){
                        inc = false;
                    }
                    else{
                        dec = false;
                    }
                }
                
                if (inc || dec){
                    return true;
                }
            }
            return false;
        } 
    
}
