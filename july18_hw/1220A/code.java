import java.util.Scanner;
// cards problem
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        String s=sc.next();
        char[] chars = s.toCharArray();
        
        // make freq list from chars 
        int cnt0 =0;
        int cnt1 =0;
        for (char ch : chars){
            if (ch== 'z'){
                cnt0++;
            }
            if (ch== 'n'){
                cnt1++;
            }
        }
        for (int i=0;i<cnt1;i++){
            System.out.println(1+" ");
        }
        for (int i=0;i<cnt0;i++){
            System.out.println(0+" ");
        }
    }
}
