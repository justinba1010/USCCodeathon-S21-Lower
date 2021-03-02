import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        //need to eat the \n at the end of the second number
        input.nextLine();
        String[] board = new String[y];
        for(int i = 0; i < y; i++)
        {
            board[i] = input.nextLine();
            // System.out.println(board[i]);
        }
        int total = 0;
        for(int i = 0; i < y; i++)
        {
            //check left side
            if(board[i].charAt(1) == '.')
            {
                total++;
            }
            
            //check right side
            if(board[i].charAt(x-2) == '.')
            {
                total++;
            }
        }
        
        for(int i = 0; i < x; i++)
        {
            //check top side
            if(board[1].charAt(i) == '.')
            {
                total++;
            }
            
            //check bottom side
            if(board[y-2].charAt(i) == '.')
            {
                total++;
            }
        }
        System.out.println(total);
        
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}