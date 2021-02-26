import java.io.*;
import java.util.*;

public class NaiveSolution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int numSides = input.nextInt();
        int[] sideArray = new int[numSides];
        int jumpSize = input.nextInt();
        int currentSide = 0;
        sideArray[0] = 1;
        jumpSize = jumpSize % numSides;
        // System.out.println(sideArray);
        currentSide += jumpSize;
        currentSide = currentSide % numSides;
        sideArray[currentSide] = 1;
        while(currentSide != 0)
        {
            currentSide += jumpSize;
            currentSide = currentSide % numSides;
            sideArray[currentSide] = 1;
            // if (currentSide == 0)
            //     break;
            // for (int i = 0; i < sideArray.length;i++ ) {
            //     System.out.print(sideArray[i] + " ");
            // }
        }
        int count = 0;
        for (int i = 0; i < sideArray.length;i++ ) {
            if(sideArray[i]== 0)
            {
                count += 1;
            }
        }
        System.out.println(count);

    }
}