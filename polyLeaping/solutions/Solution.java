import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int numSides = input.nextInt();
        int jumpSize = input.nextInt();
        int currentSide = 0;

        jumpSize = jumpSize % numSides;
        int answer = numSides -1;
        while(currentSide != numSides)
        {
            currentSide += jumpSize;
            currentSide = currentSide % numSides;
            if (currentSide == 0)
                break;
            answer -= 1;
        }
        System.out.println(answer);

    }
}