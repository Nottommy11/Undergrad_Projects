package calculator.device;

/**
 * This is an interface for the AdvanceCalc class. This interface outlines 
 * the advanced functions to be used by the Calculator. Those functions 
 * include raising a base number to a specified power and finding the 
 * square root of a value.
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

interface AdvanceMath {
    
    /** 
     * Receives the base and exponent to set the currentValue to 
     * the result of the equation
     * This method uses the Math library
     * 
     * @param base     The base number to be raised to a given power
     * @param exponent The exponent that determines the power the base is raised to
     */
    void pow(double base, double exponent);

    /**
     * Calculates the square root of the currentValue and sets the 
     * currentValue to the result
     * This method uses the Math library
     */
    void sqrt();
}
