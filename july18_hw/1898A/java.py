import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t= sc.nextInt();
        
        for (int test=0; test<t;test++){
            int n = sc.nextInt();
            int k = sc.nextInt();
            String s = sc.next();
            char[] string =s.toCharArray();
            
            int b = 0;
            for (char ch : string) {
                if (ch == 'B') {
                    b++;
                }
                
            }
            
            if (b==k){
                System.out.println(0);
            }
            else{
                char c;
                if (b<k){
                    c = 'A';
                }
                else{
                    c='B';
                }
                
                int cnt = Math.abs(k-b);
                int ind = 0;
                
                for (int i=0;i<n;i++){
                    if (string[i]==c){
                        cnt--;
                        if (cnt==0){
                            ind = i;
                            break;
                        }
                    }
                }
                System.out.println(1);
                if (c=='A'){
                    System.out.println((ind+1)+" "+"B");
                }
                else{
                    System.out.println((ind+1)+" "+"A");
                }
            }
            
        }
        
    }
}
