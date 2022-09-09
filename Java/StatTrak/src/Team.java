/** 
 * The Team class stores team data including the name
 * and players of the each team. It can also display
 * team and player level statistics.
 * GitHub: https://github.com/Nottommy11/StatTrak_CSC160
 * 
 * @author Thomas Marxsen
 * @since 2022.02.18
 * @version 1.0 beta
 */
public class Team {

    /**
     * Field storing the team's name
     */
    private String name;

    /**
     * Player object: player1
     */
    private Player player1;

    /**
     * Player object: player2
     */
    private Player player2;

    /**
     * Default Constructor for a Team object
     */
    public Team(){
        name = null;
        player1 = new Player();
        player2 = new Player();
    }

    /**
     * Overload Constructor for a Team object
     * 
     * @param name The team's name
     */
    public Team(String name){
        this();
        this.name = name;
    }
    
    /** 
     * Used to set team name
     * 
     * @param name The team's name
     */
    public void setName(String name){
        this.name = name;
    }
    
    /** 
     * Used to return the team name
     * 
     * @return String The team's name
     */
    public String getName(){
        return name;
    }
    
    /** 
     * Used to create a Player object, that being player1
     * 
     * @param name   The player's name
     * @param number The player's number
     */
    public void setPlayer1(String name, int number){
        player1.setName(name);
        player1.setNumber(number);
    }
    
    /** 
     * Used to return the player1
     * 
     * @return Player The player1 object
     */
    public Player getPlayer1(){
        return player1;
    }
    
    /** 
     * Used to create a Player Object, that being player2
     * 
     * @param name   The player's name
     * @param number The player's number
     */
    public void setPlayer2(String name, int number){
        player2.setName(name);
        player2.setNumber(number);
    }
    
    /** 
     * Used to return the player2
     * 
     * @return Player The player2 object
     */
    public Player getPlayer2(){
        return player2;
    }
    
    /** 
     * Used to return the total points for each player to
     * calculate the team's total points
     * 
     * @return int The team's total points
     */
    public int getTeamPoints(){
        return (player1.getTotalPoints() + player2.getTotalPoints());
    }
    
    /** 
     * Used to return the total common fouls for each player
     * to calculate the team's total fouls
     * 
     * @return int The team's total common fouls
     */
    public int getTeamFouls(){
        return (player1.getFouls_Common() + player2.getFouls_Common());
    }

    /**
     * Used to list players with their number and name
     */
    public void listPlayers(){
        System.out.println("1 = " + "#" + player1.getNumber() + " " + player1.getName());
        System.out.println("2 = " + "#" + player2.getNumber() + " " + player2.getName());
    }

    /**
     * Used to display the team's stats including team name,
     * fouls, and points
     */
    public void displayStats_Quick(){
        System.out.println(name + " | Fouls : " + getTeamFouls() + " | Points : " + getTeamPoints());
    }

    /**
     * Used to display full team stats for each player.
     * Calls on the player's method for displaying full stats
     */
    public void displayStats_Basic(){
        System.out.println("Number  Points  Fouls  FGM  FGA  FG%  3PM  3PA  3P%  FTM  FTA  FT%");
        player1.displayStats_Basic();
        player2.displayStats_Basic();
    }
}
