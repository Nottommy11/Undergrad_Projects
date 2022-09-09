/** 
 * The Player class stores data regarding the player's
 * name, number, and various basketball statistics.
 * It can calculate totals and percentages for those
 * statistics and display those statistics.
 * GitHub: https://github.com/Nottommy11/StatTrak_CSC160
 * 
 * @author Thomas Marxsen
 * @since 2022.02.15
 * @version 1.0 beta
 */
public class Player {

    /**
     * Field storing the player's name
     */
    private String name;

    /**
     * Field storing the player's number
     */
    private int number;

    /**
     * Field storing the number of free throws made
     */
    private int freeThrow;

    /**
     * Field storing the number of two point field goals made
     */
    private int fieldGoal_2pt;

    /**
     * Field storing the number of three point field goals made
     */
    private int fieldGoal_3pt;

    /**
     * Field storing the number of free throws attempted
     */
    private int attempts_freeThrows;

    /**
     * Field storing the number of two point field goals attempted
     */
    private int attempts_2pt;

    /**
     * Field storing the number of three point field goals attempted
     */
    private int attempts_3pt;

    /**
     * Field storing the number of common fouls committed
     */
    private int foul_Common;

    /**
     * Field storing the number of flagrant fouls committed
     */
    private int foul_Flagrant;

    /**
     * Field storing the number of technical fouls committed
     */
    private int foul_Technical;

    /**
     * Default Constructor for Player object
     */
    public Player(){
        name = null;
        number = 0;

        freeThrow = 0;
        fieldGoal_2pt = 0;
        fieldGoal_3pt = 0;

        attempts_freeThrows = 0;
        attempts_2pt = 0;
        attempts_3pt = 0;

        foul_Common = 0;
        foul_Flagrant = 0;
        foul_Technical = 0;
    }

    /**
     * Overload Constructor for Player Object
     * 
     * @param name   The player's name
     * @param number The player's number
     */
    public Player(String name, int number){
        this();             //Calls default constructor
        this.name = name;
        this.number = number;
    }
    
    /** 
     * Used to set the player name
     * 
     * @param name The player's name
     */
    public void setName(String name){
        this.name = name;
    }
    
    /** 
     * Used to get the player's name
     * 
     * @return String The player's name
     */
    public String getName(){
        return name;
    }
    
    /** 
     * Used to set the player's number
     * 
     * @param number The player's number
     */
    public void setNumber(int number){
        this.number = number;
    }
    
    /** 
     * Used to get the player's number
     * 
     * @return int The player's number
     */
    public int getNumber(){
        return number;
    }
    
    /** 
     * Switch statement that increases attempts of the type of shot and
     * increases makes if made is true
     * 
     * @param shotType The shot type (3, 4, 5)
     * @param made     Boolean value; if true, basket is made
     */
    public void setShotAttempt(int shotType, boolean made){

        switch(shotType){
            case 3:
                if(made) freeThrow++;      //Could do freeThrow += made ? 1 : 0
                attempts_freeThrows++;
                break;
            case 4:
                if(made) fieldGoal_2pt++;
                attempts_2pt++;
                break;
            case 5:
                if(made) fieldGoal_3pt++;
                attempts_3pt++;
                break;
            default:
                System.out.println("Invalid shot type. Must be (1, 2, 3). You entered: " + shotType);
        }
    }
    
    /** 
     * Field goal makes includes two point and three point makes
     * 
     * @return int The player's number of two point and three point field goals made
     */
    public int getFieldGoal_Makes(){
        return (fieldGoal_2pt + fieldGoal_3pt);
    }

    /** 
     * Field goal attempts includes two point and three point attempts
     * 
     * @return int The player's number of two point and three point field goals attempted
     */
    public int getFieldGoal_Attempts(){
        return (attempts_2pt + attempts_3pt);
    }
    
    /** 
     * Calculate total points by adding one point free throws, two point field goals,
     * and three point field goals
     * 
     * @return int The player's total points
     */
    public int getTotalPoints(){
        return freeThrow + (fieldGoal_2pt * 2) + (fieldGoal_3pt * 3);
    }
    
    /** 
     * Calculate free throw percentage as makes divided by attempts
     * multiplied by 100
     * 
     * @return double The player's free throw percentage
     */
    public double getFreeThrowPercent(){

        if((attempts_freeThrows) == 0) return 0;

        return ( (double) freeThrow / attempts_freeThrows) * 100;   //Needed to cast it to work
    }
    
    /** 
     * Calculate field goal percent as field goal makes divided by attempts
     * multiplied by 100. Field goal makes and attempts are the sum of 
     * two point and three point field goals
     * 
     * @return double The player's field goal percentage
     */
    public double getFieldGoalPercent(){

        if((attempts_2pt + attempts_3pt) == 0) return 0;

        return ( (double) getFieldGoal_Makes() / getFieldGoal_Attempts()) * 100;
    }
    
    /** 
     * Calculate three point percentage as makes divided by attempts
     * multiplied by 100
     * 
     * @return double The player's three point percentage
     */
    public double getThreePointPercent(){

        if((attempts_3pt) == 0) return 0;

        return ( (double) fieldGoal_3pt / attempts_3pt) * 100;
    }
    
    /** 
     * Switch statement that increases the foul type as indicated by the
     * foulType parameter
     * 
     * @param foulType The foul type (0, 1, 2)
     */
    public void setFouls(int foulType){

        switch(foulType){
            case 0:
                foul_Common++;
                break;
            case 1:
                foul_Flagrant++;
                break;
            case 2:
                foul_Technical++;
                break;
            default:
                System.out.println("Invalid foul type. Must be (1, 2, 3). You entered: " + foulType);
        }
    }
    
    /** 
     * Used to get the common fouls value
     * 
     * @return int The player's number of common fouls
     */
    public int getFouls_Common(){
        return foul_Common;
    }
    
    /** 
     * Used to get the flagrant fouls value
     * 
     * @return int The player's number of flagrant fouls
     */
    public int getFouls_Flagrant(){
        return foul_Flagrant;
    }
    
    /** 
     * Used to get the technical fouls value
     * 
     * @return int The player's number of technical fouls
     */
    public int getFouls_Technical(){
        return foul_Technical;
    }

    /**
     * Display basic player stats including number, name, points,
     * and all types of fouls
     */
    public void displayStats_Quick(){
        System.out.println("#" + number + " | " + name + " | Points: " + getTotalPoints());
        System.out.printf("%5s %3d\n", "Common: ", foul_Common);
        System.out.printf("%5s %1d\n", "Flagrant: ", foul_Flagrant);
        System.out.println("Technical: " + foul_Technical);
    }

    /**
     * Display full player stats that includes every shot types makes,
     * attempts, and percentage
     */
    public void displayStats_Basic(){
        System.out.printf("%1s %2d %7d %6d %6d %4d %4.0f %4d %4d %4.0f %4d %4d %4.0f\n", "#", number, getTotalPoints(), foul_Common, getFieldGoal_Makes(), getFieldGoal_Attempts(), getFieldGoalPercent(), fieldGoal_3pt, attempts_3pt, getThreePointPercent(), freeThrow, attempts_freeThrows, getFreeThrowPercent());
    }
}