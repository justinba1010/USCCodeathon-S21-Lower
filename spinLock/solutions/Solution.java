import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        input.nextLine();
        String secret = input.nextLine();
        String[] dials = new String[y];
        for(int i = 0; i < y; i++)
        {
            dials[i] = input.nextLine();
        }
        int bestCost = 10000000;
        int bestColumn = -1;
        // System.out.println("secret " + secret);
        for(int i = 0; i < x; i++)
        {
            int currentCost = 0;
            // System.out.println("column: " + i);
            for(int j = 0; j < y; j++)
            {
                int pos1 = dials[j].indexOf(secret.charAt(j));
                int cost1 = Math.abs(pos1 - i);
                int cost2 = x - cost1;
                // System.out.println("cost1 " + cost1);
                // System.out.println("cost2 " + cost2);
                currentCost += Math.min(cost1, cost2);
            }
            if(currentCost < bestCost)
            {
                bestCost = currentCost;
                bestColumn = i;
            }
        }
        System.out.println(bestColumn + " " + bestCost);
        

    }
}