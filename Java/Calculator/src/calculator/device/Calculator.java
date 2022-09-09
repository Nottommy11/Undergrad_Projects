package calculator.device;

/**
 * The base class for the types of calculators. The types include the 
 * Standard and Advanced Calculators. The Calculator base class contains 
 * basic calculator functions such as clear, addition, subtraction, 
 * multiplication, and division. 
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

public abstract class Calculator implements BasicMath {
    
    /**
     * Current Value of the calculator
     */
    protected double currentValue;

    /**
     * Default constructor
     */
    Calculator(){
        this.currentValue = 0.00;
    }

    /**
     * Sets the currentValue to 0.00 and displays the value
     */
    public void clear(){

        this.currentValue = 0.00;

        System.out.println("Clear = " + currentValue);
    };
    
    /** 
     * Adds the input value to the currentValue and sets the 
     * currentValue to the result
     * 
     * @param input User supplied value
     */
    @Override
    public void add(double input){

        System.out.println(currentValue + " + " + input + " = " + (currentValue += input));
    };
    
    /** 
     * Subtracts the input value from the currentValue and sets 
     * the currentValue to the result
     * 
     * @param input User supplied value
     */
    @Override
    public void subtract(double input){

        System.out.println(currentValue + " - " + input + " = " + (currentValue -= input));
    };
    
    /** 
     * Multiplies the currentValue by the input value and sets 
     * the currentValue to the result
     * 
     * @param input User supplied value
     */
    @Override
    public void multiply(double input){

        System.out.println(currentValue + " * " + input + " = " + (currentValue *= input));
    };

    /** 
     * Divides the currentValue by the input and sets the 
     * currentValue to the result
     * 
     * @param input User supplied value
     */
    @Override
    public void divide(double input){

        System.out.println(currentValue + " / " + input + " = " + (currentValue /= input));
    };
}
