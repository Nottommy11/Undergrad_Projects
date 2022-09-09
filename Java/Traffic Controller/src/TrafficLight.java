/** 
 * Traffic Light class that gives the objects 
 * three different states including red, 
 * yellow, and green. Those states can 
 * be changed by a boolean value.
 * GitHub: https://github.com/Nottommy11/TrafficController_CSC160.git
 * 
 * @author Thomas Marxsen
 * @since 2022.02.25
 * @version 1.0 beta
 */
public class TrafficLight {
    
    /**
     * Boolean value identifying if the 
     * traffic's light current color is red.
     */
    private boolean red;

    /**
     * Boolean value identifying if the 
     * traffic's light current color is yellow.
     */
    private boolean yellow;

    /**
     * Boolean value identifying if the 
     * traffic's light current color is green.
     */
    private boolean green;

    /**
     * BLACK = "\033[0;27m" <br/>
     * All of these have the form \033[XXXm where XXX is a series of semicolon-seperated parameters. <br/>
     * 0 = Reset ANSI escape sequences
     */
    private final static String BLACK = "\033[0;27m";

    /**
     * RED = "\033[31;7m" <br/>
     * All of these have the form \033[XXXm where XXX is a series of semicolon-seperated parameters. <br/>
     * 31 = Red ANSI escape sequences <br/>
     * 7 = Reverse Video ANSI escape sequences
     */
    private final static String RED = "\033[31;7m";

    /**
     * YELLOW = "\033[33;7m" <br/>
     * All of these have the form \033[XXXm where XXX is a series of semicolon-seperated parameters. <br/>
     * 33 = Yellow ANSI escape sequences <br/>
     * 7 = Reverse Video ANSI escape sequences
     */
    private final static String YELLOW = "\033[33;7m";

    /**
     * GREEN = "\033[32;7m" <br/>
     * All of these have the form \033[XXXm where XXX is a series of semicolon-seperated parameters. <br/>
     * 32 = Green ANSI escape sequences <br/>
     * 7 = Reverse Video ANSI escape sequences
     */
    private final static String GREEN = "\033[32;7m";
    
    /**
     * Default constructor for a traffic light.
     */
    public TrafficLight(){
        setRedOn();
    }

    /**
     * Method to reset the light to off.
     */
    public void setLightsOff(){
        red = false;
        yellow = false;
        green = false;
    }

    /** 
     * Method to identify if the light is red.
     * 
     * @return boolean Return true if the light is red.
     */
    public boolean isRed(){
        return red;
    }

    /**
     * Method to set the traffic light color to red.
     */
    public void setRedOn(){
        setLightsOff();
        red = true;
    }
    
    /** 
     * Method to identify if the light is yellow.
     * 
     * @return boolean Return true if the light is yellow.
     */
    public boolean isYellow(){
        return yellow;
    }

    /**
     * Method to set the traffic light color to yellow.
     */
    public void setYellowOn(){
        setLightsOff();
        yellow = true;
    }
    
    /** 
     * Method to identify if the light is green.
     * 
     * @return boolean Return true if the light is green.
     */
    public boolean isGreen(){
        return green;
    }

    /**
     * Method to set the traffic light color to green.
     */
    public void setGreenOn(){
        setLightsOff();
        green = true;
    }

    /**
     * Method displays the name of the color 
     * and that name has a colored background 
     * matching the color. Used to display the 
     * current state of the traffic light.
     */
    public void displayLight(){

        if(red){
            System.out.print(RED + "Red" + BLACK + "\n");
        }
        else if(yellow){
            System.out.print(YELLOW + "Yellow" + BLACK + "\n");
        }
        else if(green){
            System.out.print(GREEN + "Green" + BLACK + "\n");
        }
        else{
            System.out.print("LIGHTS ARE OFF\n");
        }
    }
}
