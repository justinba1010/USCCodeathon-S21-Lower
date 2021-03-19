import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner input = new Scanner(System.in);
        int p = input.nextInt();
        int n = input.nextInt();
        input.nextLine();
        ArrayList<String> processes = new ArrayList<String>();

        for (int i = 0; i < p; i++) {
            processes.add(input.next());
        }
        input.nextLine();
        int pos = 0;
        while (pos < n) {
            // System.out.println(processes);
            if(processes.get(0).endsWith("TEMP"))
            {
                processes.remove(0);
                continue;
            }
            else if(processes.get(0).endsWith("DARK"))
            {
                break;
            }
            else if(processes.get(0).endsWith("HUNGRY"))
            {
                processes.remove(0);
                processes.remove(0);
                continue;
            }
            int num = input.nextInt();
            pos += 1;
            // System.out.println(num);
            String current = processes.remove(num % processes.size());
            processes.add(0, current);

        }
        System.out.println(processes.get(0));
    }
}