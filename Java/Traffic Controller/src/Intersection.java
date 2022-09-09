/** 
 * Intersection class that contains 4 traffic 
 * lights. The lights are described by the 
 * direction of the street. The color of the 
 * lights can be changed by calling on the related 
 * methods in the Traffic Light class.
 * GitHub: https://github.com/Nottommy11/TrafficController_CSC160.git
 * 
 * @author Thomas Marxsen
 * @since 2022.02.28
 * @version 1.0 beta
 */
public class Intersection {
    
    /**
     * Field for the intersection's name. 
     * Two street names is the expected input.
     * Example: Colfax and 16th St
     */
    private String name;

    /**
     * The eastbound street's traffic light.
     */
    private TrafficLight eastbound;

    /**
     * The westbound street's traffic light.
     */
    private TrafficLight westbound;

    /**
     * The northbound street's traffic light.
     */
    private TrafficLight northbound;

    /**
     * The southbound street's traffic light.
     */
    private TrafficLight southbound;

    /**
     * The default constructor for creating an intersection 
     * object that contains four traffic lights.
     */
    public Intersection(){
        name = null;
        eastbound = new TrafficLight();
        westbound = new TrafficLight();
        northbound = new TrafficLight();
        southbound = new TrafficLight();
    }

    /**
     * The overload constructor that allows the user to 
     * name the intersection.
     * 
     * @param name The name of the intersection, input from the user.
     */
    public Intersection(String name){
        this();
        this.name = name;
    }

    /** 
     * Method to return the name of the intersection.
     * 
     * @return String The name of the intersection.
     */
    public String getName(){
        return name;
    }

    /**
     * This method will find the current state of 
     * the traffic light and change the related 
     * traffic lights.
     * 
     * If one traffic light is green, then that street's 
     * traffic lights will turn yellow.
     * 
     * If one traffic light is yellow, then that street's 
     * traffic lights will turn red, and the other street's
     * traffic lights will turn green.
     * 
     * If all traffic lights are red, one street's 
     * traffic lights will turn green.
     */
    public void switchTraffic(){

        if(eastbound.isGreen()){
            eastbound.setYellowOn();
            westbound.setYellowOn();
        }
        else if(eastbound.isYellow()){
            eastbound.setRedOn();
            westbound.setRedOn();
            northbound.setGreenOn();
            southbound.setGreenOn();
        }
        else if(northbound.isGreen()){
            northbound.setYellowOn();
            southbound.setYellowOn();
        }
        else if(northbound.isYellow()){
            northbound.setRedOn();
            southbound.setRedOn();
            eastbound.setGreenOn();
            westbound.setGreenOn();
        }
        else if(eastbound.isRed() && northbound.isRed()){
            northbound.setRedOn();
            southbound.setRedOn();
            eastbound.setGreenOn();
            westbound.setGreenOn();
        }
    }

    /**
     * This method will turn all traffic lights red.
     */
    public void stopTraffic(){
        eastbound.setRedOn();
        westbound.setRedOn();
        northbound.setRedOn();
        southbound.setRedOn();
    }

    /**
     * This method displays the color of each traffic light.
     */
    public void displayLights(){

        System.out.print("Eastbound is ");
        eastbound.displayLight();
        System.out.print("Westbound is ");
        westbound.displayLight();
        System.out.print("Northbound is ");
        northbound.displayLight();
        System.out.print("Southbound is ");
        southbound.displayLight();
    }
}
