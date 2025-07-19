import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        
        for (int test=0;test<t;test++){
            int n = Integer.parseInt(sc.nextLine());
            String[] input = sc.nextLine().split(" ");
            List<Integer> a = new ArrayList<>();
            for (String s : input) {
                a.add(Integer.parseInt(s));
            }
            
            Map<Integer, Integer> freq = new HashMap<>();
            for (int num : a) {
                freq.put(num, freq.getOrDefault(num, 0) + 1);
            }
            int distinct = freq.size();
            int max_freq = Collections.max(freq.values());
            
            if (distinct==max_freq){
                System.out.println(distinct-1);
            }
            else{
                System.out.println(Math.min(distinct,max_freq));
            }
        }
    }
}
