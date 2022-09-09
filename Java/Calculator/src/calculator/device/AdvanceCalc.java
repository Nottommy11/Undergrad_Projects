package calculator.device;

import java.lang.Math;

/**
 * The Advanced Calculator extends the Calculator class. The Advanced Calculator 
 * includes more functionality to the Calculator such as raising a base number to 
 * a specified power and finding the square root of a value.
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

public class AdvanceCalc extends Calculator implements AdvanceMath{
    
    public AdvanceCalc(){};
    
    /** 
     * Receives the base and exponent to set the currentValue to 
     * the result of the equation
     * This method uses the Math library
     * 
     * @param base     The base number to be raised to a given power
     * @param exponent The exponent that determines the power the base is raised to
     */
    @Override
    public void pow(double base, double exponent){

        System.out.println(base + " ^ " + exponent + " = " + (currentValue = Math.pow(base, exponent)));
    };

    /**
     * Calculates the square root of the currentValue and sets the 
     * currentValue to the result
     * This method uses the Math library
     */
    @Override
    public void sqrt(){

        System.out.println("Sqrt(" + currentValue + ") = " + (currentValue = Math.sqrt(currentValue)));
    };
}
