import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner input = new Scanner(System.in);
        int cases = input.nextInt();

        // purposely done in a way that 145/146 students would try
        for (int i = 0; i < cases; i++) {
            int cardCount = input.nextInt();
            input.nextLine();
            String[] cards = input.nextLine().split(" ");
            String values = "";

            for (int j = 0; j < cards.length; j++) {
                values += cards[j].charAt(0);
            }
            // System.out.println(values);
            int points = 0;
            while (values.length() > 0) {
                // System.out.println("values before " + values);
                char checkingValue = values.charAt(0);
                int count = countOccurrences(values, checkingValue);
                // System.out.println("found " + checkingValue + ", occurred " + count);
                values = values.replaceAll("" + checkingValue, "");
                if('2' <= checkingValue && checkingValue <= '9'){
                    if (count == 3)
                        points += 15;
                    else if (count == 4)
                        points += 20;
                }
                else if("JQK0".contains(""+checkingValue))
                {
                    // System.out.println(checkingValue + " was found " + count);

                    if (count == 3)
                        points += 30;
                    else if (count == 4)
                        points += 40;
                }
                else if (checkingValue == 'A') {
                    if (count == 3)
                        points += 45;
                    else if (count == 4)
                        points += 60;
                }
                // System.out.println(points);
            }
            System.out.println(points);

        }
    }

    public static int countOccurrences(String word, char value) {
        int count = 0;
        for (int i = 0; i < word.length(); i++)
        {
            if(word.charAt(i) == value)
                count++;

        }
        return count;
    }
}