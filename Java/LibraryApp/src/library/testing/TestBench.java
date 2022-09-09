package library.testing; // keeping the test bench logic separate

import java.util.ArrayList;
import java.util.List;

import library.inventory.*; // the wildcard * will import all classes & interfaces

/**
 * The TestBench class contains multiple unit testing methods for testing
 * the Inventory base (super or parent) and derived (sub or child) classes.
 * 
 * Since there should only be one TestBench running, all helper methods
 * are static.  We do not need to create a TestBench object to run the 
 * individual unit testing methods (helper methods).  
 * 
 * No other class needs to access the helper methods so all the unit testing
 * methods are defined as private. 
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.03.23
 */
public class TestBench {
	
	/**
	 * Stores all types of Library Inventory as long as it's a derived from the Inventory class.
	 */
	private static List<Inventory> libraryInventory = new ArrayList<>(); //Could use ArrayList with Inventory
	
	/**
	 * The default constructor currently isn't needed?
	 */
	//TestBench(){ //Default constructor
	//}

	/**
     * Use to display a double dash line.
     */
    private final static String doubleLine = "================================================================================================";

	/**
	 * Unit test instantiation of an Inventory reference variable (object)
	 * using the default constructor
	 */
	private static void unitTest1_Inventory_Default() {
		
		System.out.println();
		System.out.println("Start of " + Thread.currentThread().getStackTrace()[1].getMethodName()); //Display the method name
		System.out.println();

		//create an Inventory instance (object) using default constructor
		Inventory inventory = new Inventory();
		libraryInventory.add(inventory);
		displayInfo(inventory);
		
		inventory.setDescription("Inventory Item");
		inventory.setStatus(Status.RESERVE);
		inventory.setCondition(Condition.GOOD);
		displayInfo(inventory);

		//Do for other methods
		System.out.println();
		System.out.println("End of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		System.out.println(doubleLine);
	}
	
	/**
	 * Unit test instantiation of an Inventory reference variable (object)
	 * using the overload constructor
	 */
	private static void unitTest2_Inventory_Overload() {	
		
		System.out.println();
		System.out.println("Start of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		
		//create another Inventory instance (object) using overload constructor	
		Inventory inventory = new Inventory("Inventory Item", Status.CIRCULATING, Condition.NEW);
		libraryInventory.add(inventory);
		displayInfo(inventory);

		System.out.println();
		System.out.println("End of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * Unit test instantiation of a MovieAndTV reference variable (object)
	 * using the default constructor
	 */
	private static void unitTest3_MovieAndTV_Default() {
		
		System.out.println();
		System.out.println("Start of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		
		//create a MovieAndTV instance (object) using default constructor
		MovieAndTV movieAndTV = new MovieAndTV();
		libraryInventory.add(movieAndTV);
		displayInfo(movieAndTV);
		
		movieAndTV.setDescription("Movie and TV Item");
		movieAndTV.setStatus(Status.REFERENCE);
		movieAndTV.setCondition(Condition.POOR);
		displayInfo(movieAndTV);

		System.out.println();
		System.out.println("End of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		System.out.println(doubleLine);
	}

	/**
	 * This unit test is used to instantiation a Book reference variable (object)
	 * using the overload constructor
	 */
	private static void unitTest4_Book_Overload() {
		
		System.out.println();
		System.out.println("Start of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		
		//create a Book instance (object) using overload constructor
		Book book = new Book("Book Item", Status.RESERVE, Condition.FAIR);
		libraryInventory.add(book);
		displayInfo(book);

		System.out.println();
		System.out.println("End of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		System.out.println(doubleLine);
	}
	
	/**
	 * This unit test is used to instantiation a Book and MovieAndTV reference variable (object)
	 * using the overload constructor
	 */
	private static void unitTest5_Invalid_Data() {
		
		System.out.println();
		System.out.println("Start of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		
		Book book = new Book("Book Item", Status.RESERVE, Condition.POOR);	
		TestBench.displayInfo(book);
		
		book.setCost(-1);
		System.out.println("The book's cost is $" + book.getCost());
		System.out.println();
		
		MovieAndTV movieAndTV = new MovieAndTV("Movie and TV Item", Status.REFERENCE, Condition.NEW);	
		TestBench.displayInfo(movieAndTV);
		movieAndTV.setVideoGenre(VideoGenre.CHILDREN);
		System.out.println("The Movie or TV item is a " + movieAndTV.getVideoGenre() + " show/movie");

		System.out.println();
		System.out.println("End of " + Thread.currentThread().getStackTrace()[1].getMethodName());
		System.out.println();
		System.out.println(doubleLine);
	}
		
	/**
	 * Display the Inventory reference variable's id, type, status, and description
	 * 
	 * @param inventory the reference variable data to be displayed
	 */
	private static void displayInfo(Inventory inventory) {
		System.out.printf("ID: %-3d  Type: %-10s Status: %-10s Condition: %-8s Description: %3s\n",
				inventory.getId(), inventory.getType(), inventory.getStatus(), inventory.getCondition(), inventory.getDescription());
	} // end of displayInfo

	/**
	 * Display all Library Inventory stored in the ArrayList.
	 * It will display the id, type, status, and description
	 */
	private static void displayReport() {
		
		System.out.println();
		System.out.println();
		System.out.println("=================== INVENTORY REPORT ====================");
		System.out.println("ID  Type       Status       Condition  Description     ");
		System.out.println("=== ========== ============ =========  ==================");
		
		for (Inventory inventory : libraryInventory) {
			System.out.printf("%-3d %-10s %-12s %-10s %3s\n",
					inventory.getId(), inventory.getType(), inventory.getStatus(), inventory.getCondition(), inventory.getDescription());
		}
		
		System.out.println();
	} // end of displayReport method
	
	/**
	 * The test bench to regression test that the Inventory base and subclasses are
	 * working correctly.
	 * 
	 * @param args this program doesn't use command line input arguments
	 */
	public static void main(String[] args) {
		
		TestBench.unitTest1_Inventory_Default();
		TestBench.unitTest2_Inventory_Overload();
		TestBench.unitTest3_MovieAndTV_Default();
		TestBench.unitTest4_Book_Overload();
		TestBench.unitTest5_Invalid_Data();
		
		TestBench.displayReport();
		
	} // end of main method
} // end of Main class