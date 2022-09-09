/**
 * An app that allows the user to control 2 
 * intersections. The user can change the 
 * color of the lights and choose to 
 * stop all the traffic at the intersection
 * GitHub: https://github.com/Nottommy11/TrafficController_CSC160.git
 * 
 * @author Thomas Marxsen
 * @since 2022.02.25
 * @version 1.0 beta
 */
public class TrafficControllerApp {

    /**
     * First intersection
     */
    private Intersection intersection1;

    /**
     * Second intersection
     */
    private Intersection intersection2;

    /**
     * Use to display a double dash line.
     */
    private final static String doubleLine = "==================================================";

    /**
     * The program header
     */
    private void header(){
        System.out.println();
        System.out.println(doubleLine);
        System.out.println("           The Traffic Light Controller           ");
        System.out.println(doubleLine);
        System.out.println();
    }

    /**
     * Asks user for intersection names and instantiates 
     * both intersections with the overload constructor.
     */
    private void intersectionNames(){

        String input1;
        String input2;

        header();

        System.out.println("Enter The #1 Intersection Name (Example Below):");
        input1 = Input.getLine("(Street #1 and Street #2): ");
        intersection1 = new Intersection(input1);
        System.out.println();

        System.out.println("Enter The #2 Intersection Name (Example Below): ");
        input2 = Input.getLine("(Street #1 and Street #2): ");
        intersection2 = new Intersection(input2);
        System.out.println();
    }

    /**
     * Calls on the switchTraffic method to switch the 
     * color of the lights for the east-west and 
     * north-south traffic lights.
     */
    private void switchAll(){
        intersection1.switchTraffic();
        intersection2.switchTraffic();
    }

    /**
     * Calls on the stopTraffic method to turn all of 
     * the lights red.
     */
    private void stopAll(){
        intersection1.stopTraffic();
        intersection2.stopTraffic();
    }

    /**
     * Lists the intersections names and displays the current 
     * state of both directions of traffic lights. This includes 
     * four separate lights.
     */
    private void displayAll(){

        System.out.println();
        System.out.println("Intersection: " + intersection1.getName());
        intersection1.displayLights();
        System.out.println();

        System.out.println("Intersection: " + intersection2.getName());
        intersection2.displayLights();
        System.out.println();
    }
    
    /** 
     * Displays a menu listing the user's potential choices 
     * for the program.
     * 
     * @return int Returns the user's input choice.
     */
    public static int getMenuChoice(){

        int userInput;

        userInput = Input.getIntRange("Please Enter a Menu Selection: ", 0, 2);

        return userInput;
    }

    /**
     * Contains a loop that will run the program. 
     * Takes in the user's choice input and will either
     * exit the program, switch the traffic lights, or
     * stop all the traffic by turning the lights red.
     */
    private void controlTraffic(){
    
        int menuChoice;
        boolean continueSim = true;

        while(continueSim){

            header();

            System.out.println("0 = Exit System");
            System.out.println("1 = Switch ALL Traffic");
            System.out.println("2 = Stop ALL Traffic");
            System.out.println();

            menuChoice = getMenuChoice();
            System.out.println();
            System.out.println(doubleLine);

            switch(menuChoice){
                case 0:
                    continueSim = false;
                    break;
                case 1:
                    switchAll();
                    displayAll();
                    break;
                case 2:
                    stopAll();
                    displayAll();
                    break;
                default:
                    System.out.println("Error code 123456789");
                    break;
            }
        }

        System.out.println();
        System.out.println("Thank you for using the Traffic Controller App!");
        System.out.println();
    }

    /** 
     * The main method that calls on the name method 
     * to get create the intersections and then calls 
     * on the traffic control loop that runs the program.
     * 
     * @param args No command line input args are used for this application.
     */
    public static void main(String[] args) {

        TrafficControllerApp app = new TrafficControllerApp();

        app.intersectionNames();
        app.controlTraffic();
    }
}
