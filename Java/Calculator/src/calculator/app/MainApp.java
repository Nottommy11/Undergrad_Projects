package calculator.app; // keeping the main app logic separate

import calculator.device.*;

/** 
 * The MainApp class contains multiple unit testing methods for testing
 * the Calculator base (super or parent) and derived (sub or child) classes.
 * 
 * The methods of the Standard and Advanced Calculators will be tested.
 * 
 * Since there should only be one MainApp running, all helper methods
 * are static.  We do not need to create a MainApp object to run the 
 * individual unit testing methods (helper methods).
 * 
 * No other class needs to access the helper methods so all the unit testing
 * methods are defined as private. 
 * 
 * GitHub: https://github.com/Nottommy11/CalculatorApp_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.11
 */

public class MainApp {

	/**
     * Use to display a double dash line.
     */
    private final static String doubleLine = ("=========================");

	/**
	 * Creates a Standard Calculator Object
	 */
	private final static StandardCalc calculator = new StandardCalc();

	/**
	 * Creates an Advanced Calculator Object
	 */
	private final static AdvanceCalc AdvCalculator = new AdvanceCalc();

	/**
	 * Default Constructor for MainApp
	 */
	//MainApp(){};

	/**
	 * Displays the heading for the MainApp
	 */
	private static void displayHeader() {

		System.out.println();
		System.out.println(doubleLine);
		System.out.println("    Simple Calculator    ");
		System.out.println(doubleLine);
	}

	/**
	 * Addition test of a Standard Calculator Object
	 */
	private static void unitTest1_Test_Add() {
		
		System.out.println();
		System.out.println("Testing Add:");
		System.out.println();
		
		calculator.add(10);
		
		System.out.println();
		System.out.println("End of Addition Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Subtraction test of a Standard Calculator Object
	 */
	private static void unitTest2_Test_Subtract() {
		
		System.out.println();
		System.out.println("Testing Subtract:");
		System.out.println();
		
		calculator.subtract(5.5);
		
		System.out.println();
		System.out.println("End of Subtraction Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Multiplication test of a Standard Calculator Object
	 */
	private static void unitTest3_Test_Multiply() {
		
		System.out.println();
		System.out.println("Testing Multiply:");
		System.out.println();
		
		calculator.multiply(1);
		
		System.out.println();
		System.out.println("End of Multiplication Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Division test of a Standard Calculator Object
	 */
	private static void unitTest4_Test_Divide() {
		
		System.out.println();
		System.out.println("Testing Divide:");
		System.out.println();
		
		calculator.divide(1);
		
		System.out.println();
		System.out.println("End of Division Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Memory Addition test of a Standard Calculator Object
	 */
	private static void unitTest5_Test_MemoryAdd() {
		
		System.out.println();
		System.out.println("Testing M+:");
		System.out.println();
		
		calculator.memoryAdd();
		
		System.out.println();
		System.out.println("End of M+ Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Clearing the currentValue test of a Standard Calculator Object
	 */
	private static void unitTest6_Test_Clear() {
		
		System.out.println();
		System.out.println("Testing Clear:");
		System.out.println();
		
		calculator.clear();
		
		System.out.println();
		System.out.println("End of Clear Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Memory Subtraction test of a Standard Calculator Object
	 */
	private static void unitTest7_Test_MemorySubtract() {
		
		System.out.println();
		System.out.println("Testing M-:");
		System.out.println();
		
		calculator.memorySubtract();
		
		System.out.println();
		System.out.println("End of M- Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Memory Recall test of a Standard Calculator Object
	 */
	private static void unitTest8_Test_MemoryRecall() {
		
		System.out.println();
		System.out.println("Testing MR:");
		System.out.println();
		
		calculator.add(200.2);
		calculator.memoryRecall();
		
		System.out.println();
		System.out.println("End of MR Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Memory Clear test of a Standard Calculator Object
	 */
	private static void unitTest9_Test_MemoryClear() {
		
		System.out.println();
		System.out.println("Testing MC:");
		System.out.println();
		
		calculator.memoryClear();
		
		System.out.println();
		System.out.println("End of MC Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Power test of an Advanced Calculator Object
	 */
	private static void unitTest10_Test_POW() {
		
		System.out.println();
		System.out.println("Testing POW:");
		System.out.println();
		
		calculator.clear();
		AdvCalculator.pow(2, 4);
		
		System.out.println();
		System.out.println("End of POW Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Square Root test of an Advanced Calculator Object
	 */
	private static void unitTest11_Test_Sqrt() {
		
		System.out.println();
		System.out.println("Testing Sqrt:");
		System.out.println();
		
		AdvCalculator.sqrt();
		
		System.out.println();
		System.out.println("End of Sqrt Test");
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * The main app test to verify that all methods for the 
	 * Standard and Advanced Calculator classes work correctly
	 * 
	 * @param args this program doesn't use command line input arguments
	 */
	public static void main(String[] args) {
		
		MainApp.displayHeader();
		MainApp.unitTest1_Test_Add();
		MainApp.unitTest2_Test_Subtract();
		MainApp.unitTest3_Test_Multiply();
		MainApp.unitTest4_Test_Divide();
		MainApp.unitTest5_Test_MemoryAdd();
		MainApp.unitTest6_Test_Clear();
		MainApp.unitTest7_Test_MemorySubtract();
		MainApp.unitTest8_Test_MemoryRecall();
		MainApp.unitTest9_Test_MemoryClear();
		MainApp.unitTest10_Test_POW();
		MainApp.unitTest11_Test_Sqrt();
		
	} // end of main method
} // end of Main class