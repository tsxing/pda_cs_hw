import java.util.*;
import java.math.*;
//https://codeforces.com/problemset/problem/1514/C
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        ArrayList<Integer> coprimes = new ArrayList<>();
        for (int x = 1; x < n; x++) {
            if (gcd(x, n) == 1) {
                coprimes.add(x);
            }
        }

        long prod = 1;
        for (int num : coprimes) {
            prod = (prod * num) % n;
        }

        if (prod != 1) {
            coprimes.remove((Integer)(int)prod); 
        }

        System.out.println(coprimes.size());
        for (int num : coprimes) {
            System.out.print(num + " ");
        }
    }

    // find gcd of two nums
    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
