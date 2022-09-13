import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.Priority;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.geometry.Insets;
import javafx.geometry.Pos;

/**
 * A simple GUI calculator that can carry out the following functions:
 * Memory clear, memory recall, memory addition, and memory subtraction.
 * Addition, subtraction, multiplication, and division.
 * Percent conversion, power of 2, power of given number, and square root.
 * Adding a decimal and negative sign.
 * Clear entry, clear, and backspace.
 * 
 * GitHub: https://github.com/Nottommy11/JavaFX_Calculator_CSC160.git
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.04.25
 */
public class JavaFXCalculator extends Application {

	/**
	 * This text field displays the calculators value
	 */
	private TextField calcDisplay;

	/**
	 * This text displays the memory value
	 */
	private Text memoryText;

	/**
	 * Stores the value resulting from computations
	 */
	private double result = 0.0;

	/**
	 * Stores the memory value, can be added to, subtracted from, used in
	 * calculations, and cleared
	 */
	private double memory = 0.0;

	/**
	 * The user's input into the calculator as a string
	 */
	private String inStr = "0";

	/**
	 * Stores the last operator's value, is used in the compute method for
	 * calculations
	 */
	private String lastOperator = " ";

	/**
	 * Used to set the inStr negative
	 */
	private String negativeNum = "";

	/**
	 * Handles any inputs from the user and uses the logic to decide what is to be
	 * done
	 * with the user's input
	 */
	EventHandler handler = evt -> { // Event handler for all the 28 Buttons

		/**
		 * Stores the value input by the user. The following logic decides the use of
		 * the input
		 */
		String currentBtnLabel = ((Button) evt.getSource()).getText();

		switch (currentBtnLabel) {
			case "0":
			case "1":
			case "2":
			case "3":
			case "4":
			case "5":
			case "6":
			case "7":
			case "8":
			case "9":
			case "(-)":
			case ".":
			case "\u2190": // Negative sign, decimal, and backspace
				if (currentBtnLabel.equals("\u2190")) { // Check if the user input a backspace

					if (inStr.length() == 1) { // If there is only one number, set the string to 0
						inStr = "0";
					} else { // Create a substring that contains 1 less than the length of the string
						inStr = inStr.substring(0, (inStr.length() - 1));
					}
				} else if (currentBtnLabel.equals(".")) { // Check if the user input a decimal

					if (!(inStr.contains("."))) { // If there isn't a decimal in the string, then add it to the end
						inStr += currentBtnLabel;
					} else { // If there is a decimal, don't do anything
						break;
					}
				} else if (inStr.equals("0")) { // Check if the string is a 0

					if (currentBtnLabel.equals("(-)")) { // If the user input a negative sign and the string is 0, set
															// the string as "-"
						inStr = "-";
					} else { // This drops the leading 0 and sets the string as the input number
						inStr = currentBtnLabel;
					}
				} else if (currentBtnLabel.equals("(-)")) { // Check if the user input a negative sign

					if (!(inStr.contains("-"))) { // If the string doesn't have a negative yet, add a "-" to the
													// beginning
						negativeNum = "-";
						inStr = negativeNum.concat(inStr);
					} else { // If there is already a negative sign, then don't do anything
						break;
					}
				} else { // Append the input number
					inStr += currentBtnLabel;
				}

				if (lastOperator == "=") { // Reset result and lastOperator
					lastOperator = " ";
					result = 0.0;
				}

				calcDisplay.setText(inStr); // Display the new string
				break;

			/**
			 * Operator Buttons:
			 * 
			 * Add | Subtract | Multiply | Divide | Equals
			 * 
			 * % | Exponent 2 | Given Exponent | Square Root
			 * 
			 * Clear Entry | Clear
			 * 
			 * Memory Clear | Memory Recall | Memory Add | Memory Subtract
			 * 
			 * In general, most cases call on compute method and set lastOperator to the
			 * operator
			 * selected. The compute method will set the input as the result and come back
			 * to this
			 * method for input. The given input is then used in the compute method with the
			 * previous set lastOperator deciding how it is used.
			 */
			// Addition
			case "+":
				compute();
				lastOperator = "+";
				break;

			// Subtraction
			case "-":
				compute();
				lastOperator = "-";
				break;

			// Multiplication
			case "x":
				compute();
				lastOperator = "*";
				break;

			// Division
			case "\u00F7":
				compute();
				lastOperator = "\u00F7";
				break;

			// Convert to percent
			case "%": // Sets the lastOperator as there isn't additional input
				lastOperator = "%";
				compute();
				lastOperator = "=";
				break;

			// Power of 2
			case "x\u00B2": // Sets the lastOperator as there isn't additional input
				lastOperator = "x\u00B2";
				compute();
				lastOperator = "=";
				break;

			// Power of given number
			case "x^x":
				compute();
				lastOperator = "x^x";
				break;

			// Square Root
			case "\u221A": // Sets the lastOperator as there isn't additional input
				lastOperator = "\u221A";
				compute();
				lastOperator = "=";
				break;

			// Equals
			case "=":
				compute();
				lastOperator = "=";
				break;

			// Clear entry
			case "CE": // Sets the string to "0" and displays that as well
				inStr = "0";
				calcDisplay.setText("0");
				break;

			// Clear
			case "C": // Sets the result to 0, string to "0" and displays that as well
				result = 0;
				inStr = "0";
				lastOperator = " ";
				calcDisplay.setText("0");
				break;

			// Memory clear
			case "MC": // Sets the memory value to 0 and displays that value
				memory = 0.0;
				memoryText.setText("Memory = " + memory + "");
				break;

			// Memory recall
			case "MR": // Brings the memory value up to be used with the user's input
				inStr = String.valueOf(memory);
				calcDisplay.setText(memory + "");
				break;

			// Memory Addition
			case "M+": // Adds the input/result value to the memory value and displays the new value
				if (!(Double.parseDouble(inStr) == 0)) { // If the input isn't 0, add that value to memory
					memory += Double.parseDouble(inStr);
				} else { // If the input is 0, use the result value to add to memory
					memory += result;
				}
				memoryText.setText("Memory = " + memory + "");
				break;

			// Memory Subtraction
			case "M-": // Subtracts the input/result value from the memory value and displays the new
						// value
				if (!(Double.parseDouble(inStr) == 0)) { // If the input isn't 0, subtract that value from memory
					memory -= Double.parseDouble(inStr);
				} else { // If the input is 0, use the result value to subtract from memory
					memory -= result;
				}
				memoryText.setText("Memory = " + memory + "");
				break;
		}
	};

	/**
	 * This method will receive a string and convert it to a double. That double is
	 * then used in calculating the result. The lastOperator will be given.
	 */
	private void compute() {

		/**
		 * The user's input, inStr, is converted to a double
		 */
		double inNum = Double.parseDouble(inStr);

		inStr = "0"; // Reset the string to "0"

		switch (lastOperator) {
			case " ": // Primarily used at the start of the program and after "="
				result = inNum;
				break;

			// Addition
			case "+":
				result += inNum;
				break;

			// Subtraction
			case "-":
				result -= inNum;
				break;

			// Multiplication
			case "*":
				result *= inNum;
				break;

			// Division
			case "\u00F7":
				result /= inNum;
				break;

			// Convert to percent
			case "%":
				result *= 100;
				break;

			// Power of 2
			case "x\u00B2":
				if (inNum != 0.0) { // If input isn't 0, use that input as the base
					result = Math.pow(inNum, 2);
				} else { // If input is 0, use the result as the base
					result = Math.pow(result, 2);
				}
				break;

			// Power of given number
			case "x^x": // Previous input/result act as the base, new input is exponent
				result = Math.pow(result, inNum);
				break;

			// Square Root
			case "\u221A":
				if (inNum != 0.0) { // If input isn't 0, use the input in the square root
					result = Math.sqrt(inNum);
				} else { // If input is 0, use the result in the square root
					result = Math.sqrt(result);
				}
				break;

			// Equals
			case "=":
				break;
		}

		calcDisplay.setText(result + ""); // Display the result
	}

	/**
	 * Sets up the UI for the program.
	 */
	@Override
	public void start(Stage primaryStage) {

		/**
		 * Creates an array of buttons
		 */
		Button[] btns; // 28 buttons

		/**
		 * Provides the labels of the buttons.
		 * 
		 * MC = Memory Clear
		 * MR = Memory Recall
		 * M+ = Memory Addition
		 * M- = Memory Subtraction
		 * 
		 * % = Convert to Percent
		 * CE = Clear Entry
		 * C = Clear
		 * \u2190 = Backspace
		 * 
		 * x\u00B2 = x Raised to the Power of 2
		 * x^x = x Raised to a Given Number
		 * \u221A = Square Root
		 * \u00F7 = Division
		 * 
		 * 7 | 8 | 9 | Multiplication
		 * 4 | 5 | 6 | Subtraction
		 * 1 | 2 | 3 | Addition
		 * (-) | 0 | . | Equals
		 * 
		 * (-) = Negative Sign
		 * . = Decimal
		 */
		String[] btnLabels = { // Labels of 28 buttons
				"MC", "MR", "M+", "M-",
				"%", "CE", "C", "\u2190",
				"x\u00B2", "x^x", "\u221A", "\u00F7",
				"7", "8", "9", "x",
				"4", "5", "6", "-",
				"1", "2", "3", "+",
				"(-)", "0", ".", "=",
		};

		calcDisplay = new TextField("0");
		calcDisplay.setEditable(false);
		calcDisplay.setAlignment(Pos.CENTER_RIGHT);

		memoryText = new Text("Memory = 0");

		/**
		 * Creates a GridPane of 4 columns
		 */
		int numCols = 4;

		/**
		 * Creates a GridPane object
		 */
		GridPane paneButton = new GridPane();
		paneButton.setPadding(new Insets(15, 0, 15, 0)); // Top, right, bottom, left
		paneButton.setVgap(5); // Vertical gap between nodes
		paneButton.setHgap(5); // Horizontal gap between nodes

		/**
		 * Sets up 4 columns of equal width
		 */
		ColumnConstraints[] columns = new ColumnConstraints[numCols];

		for (int i = 0; i < numCols; ++i) {
			columns[i] = new ColumnConstraints();
			columns[i].setHgrow(Priority.ALWAYS); // Allow column to grow
			columns[i].setFillWidth(true); // Ask nodes to fill space for column
			paneButton.getColumnConstraints().add(columns[i]);
		}

		/**
		 * Sets up the given amount buttons
		 */
		btns = new Button[btnLabels.length];

		for (int i = 0; i < btns.length; ++i) {
			btns[i] = new Button(btnLabels[i]);

			switch (btnLabels[i]) {
				case "M+":
				case "M-":
				case "MR":
				case "MC":
					btns[i].setStyle("-fx-color: orange");
					break;
				case "CE":
				case "C":
				case "\u2190":
					btns[i].setStyle("-fx-color: blue");
			}

			btns[i].setOnAction(handler); // Register event handler
			btns[i].setMaxSize(Double.MAX_VALUE, Double.MAX_VALUE); // full-width
			paneButton.add(btns[i], i % numCols, i / numCols); // control, col, row
		}

		/**
		 * Creates a BorderPane object
		 */
		BorderPane root = new BorderPane(); // Setup up the scene graph rooted at a BorderPane (of 5 zones)

		root.setPadding(new Insets(15, 15, 15, 15)); // Top, right, bottom, left
		root.setTop(calcDisplay); // Top zone contains the TextField

		root.setBottom(memoryText); // Set the memoryText to be displayed at the bottom

		root.setCenter(paneButton); // Center zone contains the GridPane of Buttons

		primaryStage.setScene(new Scene(root, 400, 400)); // Set up scene and stage
		primaryStage.setTitle("JavaFX Calculator");
		primaryStage.show();
	}

	/**
	 * Main that launches the GUI calculator
	 */
	public static void main(String[] args) {
		launch(args);
	}
}