import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        String sentence = input.nextLine();
        boolean isLower = true;
        sentence = sentence.toLowerCase();
        String answer = "";
        for(int i= 0; i < sentence.length(); i++)
        {
            if(sentence.substring(i, i+1).equals(" "))
            {
                answer += sentence.substring(i, i+1);
                continue;
            }
            if(isLower)
            {
                answer += sentence.substring(i, i+1);
                isLower = false;
            }
            else
            {
                answer += sentence.substring(i, i+1).toUpperCase();
                isLower = true;
            }
        }
        System.out.println(answer);
    }
}