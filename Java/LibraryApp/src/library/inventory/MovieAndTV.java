package library.inventory;

/**
 * The MovieAndTV class is a subclass, deriving from it's parent/base class Inventory.
 * The MovieAndTV class extends the Inventory class. 
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.03.23
*/
public class MovieAndTV extends Inventory {

	/**
	 * Default Inventory type is Inventory, but this should always get changes
	 * in the subclasses (child class / derived class).  It's final so it 
	 * can't be internally changed.
	 */
	protected final String type = "Video";
	
	/**
	 * The MoveAndTV's genre; enum Genre values are DOCUMENTARY, FAMILY, ACTION, ROMANCE, ANIMATED, and CHILDREN.
	 */
	protected VideoGenre videoGenre;

	/**
	 * The MovieAndTV's title.
	 */
	protected String title;

	/**
	 * The MovieAndTV's cost to the library.
	 */
	protected double cost;
	
	/**
	 * The MovieAndTV default constructor that calls the overload constructor
	 */
	public MovieAndTV(){
		this(null, null, null); //description, status, and condition
	}

	/**
	 * Overload constructor that allows setting the object's default fields (attributes).
	 * Also sets the object's (MovieAndTV) default fields (attributes).
	 * videoGenre is set to null.
	 * title is set to null.
	 * cost is set to 0.00.
	 * 
	 * @param description Default description of the item is null.
	 * @param status Default status is null.
	 * @param condition Default condition is null.
	 */
	public MovieAndTV(String description, Status status, Condition condition) {
		super(description, status, condition);
		this.videoGenre = null;
		this.title = null;
		this.cost = 0.00;
	}
	
	/**
	 * Get the Inventory's type.  This parent's class method has to be 
	 * overridden in the subclass otherwise we would only see the parent's 
	 * class type value of Inventory, and instead we want it to return Video.
	 */
	@Override // Whenever you override a method, you should use the @Override annotation so the compile verifies
	public String getType() {
		return this.type;
	}

	/**
	 * Get the MovieAndTV's Genre.
	 * 
	 * @return The MovieAndTV's Genre (enum DOCUMENTARY, FAMILY, ACTION, ROMANCE, ANIMATED, or CHILDREN).
	 */
	public VideoGenre getVideoGenre() {
		return this.videoGenre;
	}

	/**
	 * Set the MovieAndTV's Genre.
	 * 
	 * @param videoGenre The MovieAndTV's Genre (enum DOCUMENTARY, FAMILY, ACTION, ROMANCE, ANIMATED, or CHILDREN).
	 */
	public void setVideoGenre(VideoGenre videoGenre) {
		this.videoGenre = videoGenre;
	}

	/**
	 * Get the MovieAndTV's title.
	 * 
	 * @return The MovieAndTV's title.
	 */
	public String getTitle() {
		return this.title;
	}

	/**
	 * Set the MovieAndTV's title.
	 * 
	 * @param title The MovieAndTV's title.
	 */
	public void setTitle(String title) {
		this.title = title;
	}

	/**
	 * Get the MovieAndTV's cost.
	 * 
	 * @return The MovieAndTV's cost.
	 */
	public double getCost() {
		return this.cost;
	}

	/**
	 * Set the MovieAndTV's cost.
	 * The MovieAndTV's cost can not be negative, and if it is set it to zero.
	 * 
	 * @param cost The MovieAndTV's cost in dollars.
	 */
	public void setCost(double cost) {
		this.cost = cost;
	}
}
