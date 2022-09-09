import java.util.Scanner;

/*
Program     : Invoice App
Description : This program will allow the user to enter a selected amount
              of line items and calculate the subtotal, discount percentage,
              discount amount, and invoice total
Author      : Thomas Marxsen
Date Written: 2022.01.27
GitHub Repository: https://github.com/Nottommy11/InvoiceApp_VSC.git
*/
public class InvoiceApp {

    @SuppressWarnings("resource")
	public static void main(String[] args) {

        String choice = "y";                                    //Used for while loop
        String input = "?";                                     //Used as input string

        int numLineItems = 0;                                   //Number of line items inputted by user
        double subtotal = 0;                                    //Sum of line items
        double discountPercent = 0;                             //Applicable discount percent based on subtotal amount
        double discountAmount = 0;                              //Subtotal times applicable discount percent
        double invoiceTotal = 0;                                //Total after applicable discount

        Scanner scanLine = new Scanner(System.in);              //Scanner object named scanLine 

        // welcome the user to the program
        System.err.println();  // print a blank line
        System.out.println("==========================================");
        System.out.println("Welcome to the Invoice Total Calculator v2");
        System.out.println("==========================================");
        System.out.println();  // print a blank line

        // perform invoice calculations until choice isn't equal to "y" or "Y"
        while (choice.equalsIgnoreCase("y")) {

            //Ask for amount of line items
            System.out.print("Enter the number of line items:   ");
            input = scanLine.nextLine();
            numLineItems = Integer.parseInt(input); //Convert input to an integer
            input = "?";
            System.out.println();
            System.out.println("==========================================");
            System.out.println();

            //Ask for line item amounts
            for (int i = 1; i <= numLineItems; i++){
                System.out.print("Enter the #" + i + " line items: ");
                input = scanLine.nextLine();
                subtotal += Double.parseDouble(input);  //Convert input into a double and add to subtotal
                input = "?";
            }
            System.out.println();
            System.out.println("==========================================");
            System.out.println();

            // calculate the discount amount and total
            if (subtotal >= 200) {
                discountPercent = .2;
            } else if (subtotal >= 100) {
                discountPercent = .1;
            } else {
                discountPercent = 0.0;
            }
            discountAmount = subtotal * discountPercent;
            invoiceTotal = subtotal - discountAmount;

            //Display the subtotal, discount percent, discount amount, and invoice total
            System.out.printf("%20s: %,10.2f", "Subtotal", subtotal);
            System.out.println();
            System.out.printf("%20s: %,10.2f", "Discount Percent", discountPercent);
            System.out.println();
            System.out.printf("%20s: %,10.2f", "Discount Amount", discountAmount);
            System.out.println();
            System.out.printf("%20s: %,10.2f", "Invoice Total", invoiceTotal);
            System.out.println();
            System.out.println();
            System.out.println("==========================================");
            System.out.println();

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = scanLine.nextLine();
            System.out.println();
            System.out.println("==========================================");
            System.out.println();

            //Reset variables
            numLineItems = 0;
            subtotal = 0;
            discountPercent = 0;
            discountAmount = 0;
            invoiceTotal = 0;
        }

        //Closing
        System.out.println("Thank you for choosing the Invoice App, come again!");
    }    
}