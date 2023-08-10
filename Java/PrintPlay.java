public class Print_Play {
    public static void main(String[] args) {
        int num = 16;
        int second = 19;
        double test = 4;
        int quote = num / second; //will only print the integer value of num / test
        double quotient = num / test; //Have to explicitly make a double value if dividing a double and integer together
        System.out.println("Printing out a number inside a print statement: " + num);
        System.out.println("Printing out two numbers inside a print statement: " + num + second);
        System.out.println("Doing arithmetic inside a print statement: " + (num + second));
        //Why lines after the one above don't work, beats me. Ask TA
        System.out.println(quote);
        System.out.println(quotient);
        System.out.println("Quotient of " + num + " and " + second + ": " + quote);
        System.out.println("Quotient of " + num + " and " + test + ": " + quotient);
        /*Do not need to explicitly cast numeric values to a string value inside a print statement to do arithmetic expressions in java
         * Also do not need to explicitly cast numeric types to a string value inside a print statement, Java will automatically do the
         * casting for you.
         */
    }
}
