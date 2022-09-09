package calculator.device;

/**
 * This is an interface for the Calculator class. This interface 
 * outlines the basic functions that any calculator should be capable 
 * of. Those functions include addition, subtraction, multiplication, 
 * and division.
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

interface BasicMath {

    /** 
     * Adds the input value to the currentValue and sets the 
     * currentValue to the result
     * 
     * @param input User supplied value
     */
    void add(double input);

    /** 
     * Subtracts the input value from the currentValue and sets 
     * the currentValue to the result
     * 
     * @param input User supplied value
     */
    void subtract(double input);

    /** 
     * Multiplies the currentValue by the input value and sets 
     * the currentValue to the result
     * 
     * @param input User supplied value
     */
    void multiply(double input);

    /** 
     * Divides the currentValue by the input and sets the 
     * currentValue to the result
     * 
     * @param input User supplied value
     */
    void divide(double input);
}