import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        
        int t= sc.nextInt();
        for (int test=0;test<t;test++){
            int n=sc.nextInt();
            int a=sc.nextInt();
            int b=sc.nextInt();
            
            if (a<=b){
                System.out.println((int) Math.ceil((double) n / a));
            }
            else{
                System.out.println(1);
            }
        }
    }
}
