import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int t = scanner.nextInt();
        
        for (int i=0;i<t;i++){
            int ans = scanner.nextInt();
            int[] arr = new int[ans];
            for (int j=0; j<ans;j++){
                arr[j] = scanner.nextInt();
            }
            
            int s = findmin(arr);

            for (int j=0;j<arr.length;j++){
                if (arr[j]==s){
                    ans--;
                }
            }
            
            System.out.println(ans);
            
            
        }
        
        
        
    }
    
    public static int findmin(int[] a){
        int ans = a[0];
        for (int i=1;i<a.length;i++){
            if (a[i] < ans){
                ans = a[i];
            }
        }
        return ans;
        
    }
}
