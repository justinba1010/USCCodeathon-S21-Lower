import java.io.*;
import java.util.*;

public class Solution
{

    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);

        int caseCount = input.nextInt();
        for (int j = 0; j < caseCount; j++)
        {


            int numSides = input.nextInt();
            int jumpSize = input.nextInt();

            System.out.println(numSides - (numSides / gcd(numSides, jumpSize)));

        }


    }
    
    public static int gcd(int a, int b)
    {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}