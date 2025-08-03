import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        for (int test=0;test<t;test++){
            String a=sc.nextLine();
            String b=sc.nextLine();
            System.out.println(sol(a,b));
        }
    }
    public static int sol(String a,String b){
        int max_common =0;
        for (int i=0;i<a.length();i++){
            for (int j=0;j<b.length();j++){
                int lens = 0;
                while (i+lens<a.length() &&j+lens<b.length() && a.charAt(i + lens) == b.charAt(j + lens)){
                    lens++;
                    max_common = Math.max(max_common,lens);
                }
            }
        }
        return a.length() + b.length() -2*max_common;
    }
}
