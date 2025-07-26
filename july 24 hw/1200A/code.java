import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String input = sc.nextLine();
        char[] s = input.toCharArray();
        
        int[] ans = new int[10];
        
        for (int i=0; i<N;i++){
            if (s[i]=='L'){
                for (int j = 0; j < 10; j++) {
                    if (ans[j] == 0) {
                        ans[j] = 1;
                        break;
                    }
                }
            }
            else if (s[i] =='R'){
                for (int j = 9; j >=0; j--) {
                    if (ans[j] == 0) {
                        ans[j] = 1;
                        break;
                    }
                }
            }
            else{
                int w =s[i] -'0'; //converts to int
                ans[w]=0;
            }
        }
        
        for (int val : ans){
            System.out.print(val);
        }
    }
}
