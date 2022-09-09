package calculator.device;

/**
 * The Standard Calculator extends the Calculator class. The Standard Calculator 
 * includes more functionality to the Calculator such as storing a memory value, 
 * clearing the memory value, adding to the memory value, subtracting from the 
 * memory value, and recalling the memory value to be used in an equation.
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

public class StandardCalc extends Calculator{
    
    /**
     * This field can store a value
     */
    protected double memoryValue;

    /**
     * Default constructor. Sets the memoryValue to a default of 0.00
     */
    public StandardCalc(){

        this.memoryValue = 0.00;
    };

    /**
     * Sets the value of the memory to 0.00 and prints the value
     */
    public void memoryClear(){
        this.memoryValue = 0.00;

        System.out.println("MC = " + memoryValue);
    };

    /**
     * Adds the currentValue to the memoryValue and sets 
     * the memoryValue to the result
     */
    public void memoryAdd(){

        System.out.println(memoryValue + " M+ " + currentValue + " = " + (memoryValue += currentValue));
    };

    /**
     * Subtracts the currentValue from the memoryValue and sets 
     * the memoryValue to the result
     */
    public void memorySubtract(){

        System.out.println(memoryValue + " M- " + currentValue + " = " + (memoryValue -= currentValue));
    };

    /**
     * Adds the memoryValue to the currentValue and sets the 
     * currentValue to the result
     */
    public void memoryRecall(){

        System.out.println(currentValue + " + MR:" + memoryValue + " = " + (currentValue += memoryValue));
    };
}
