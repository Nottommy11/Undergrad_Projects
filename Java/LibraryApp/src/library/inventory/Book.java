package library.inventory;

/**
 * The Book class is a subclass, deriving from it's parent/base class Inventory.
 * The Book class extends the Inventory class. 
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.03.23
*/
public class Book extends Inventory {

	/**
	 * Default Inventory type is Inventory, but this should always get changes
	 * in the subclasses (child class / derived class).  It's final so it 
	 * can't be internally changed.
	 */
	protected final String type = "Book";
	
	/**
	 * The book's genre; enum Genre values are FICTION, NONFICTION, BIOGRAPHY, and AUTOBIOGRAPHY.
	 */
	protected BookGenre bookGenre;

	/**
	 * The book's title.
	 */
	protected String title;

	/**
	 * The book's author.
	 */
	protected String author;

	/**
	 * The book's cost to the library.
	 */
	protected double cost;

	/**
	 * The book's isbn identifier.
	 */
	protected String isbn;
	
	/**
	 * The Book default constructor that calls the overload constructor
	 */
	public Book(){
		this(null, null, null); // description, status, and condition
	}
	
	/**
	 * Overload constructor that allows setting the object's default fields (attributes).
	 * Also sets the object's (Book) default fields (attributes).
	 * bookGenre is set to null.
	 * title is set to null.
	 * author is set to null.
	 * cost is set to 0.00.
	 * isbn is set to null
	 * 
	 * @param description Default description of the item is null.
	 * @param status Default status is null.
	 * @param condition Default condition is null;
	 */
	public Book(String description, Status status, Condition condition) {
		super(description, status, condition);
		this.bookGenre = null;
		this.title = null;
		this.author = null;
		this.cost = 0.00;
		this.isbn = null;
	}
	
	/**
	 * Get the Inventory's type.  This parent's class method has to be 
	 * overridden in the subclass otherwise we would only see the parent's 
	 * class type value of Inventory, and instead we want it to return Book.
	 */
	@Override // Whenever you override a method, you should use the @Override annotation so the compile verifies
	public String getType() {
		return this.type;
	}

	/**
	 * Get the book's Genre.
	 * 
	 * @return The book's Genre (enum FICTION, NONFICTION, BIOGRAPHY, or AUTOBIOGRAPHY).
	 */
	public BookGenre getBookGenre() {
		return this.bookGenre;
	}

	/**
	 * Set the book's Genre.
	 * 
	 * @param bookGenre The book's Genre (enum FICTION, NONFICTION, BIOGRAPHY, or AUTOBIOGRAPHY).
	 */
	public void setBookGenre(BookGenre bookGenre) {
		this.bookGenre = bookGenre;
	}

	/**
	 * Get the book's title.
	 * 
	 * @return The book's title.
	 */
	public String getTitle() {
		return this.title;
	}

	/**
	 * Set the book's title.
	 * 
	 * @param title The book's title.
	 */
	public void setTitle(String title) {
		this.title = title;
	}

	/**
	 * Get the book's author.
	 * 
	 * @return The book's author.
	 */
	public String getAuthor() {
		return this.author;
	}

	/**
	 * Set the book's author.
	 * 
	 * @param author The book's author.
	 */
	public void setAuthor(String author) {
		this.author = author;
	}

	/**
	 * Get the book's cost.
	 * 
	 * @return The book's cost.
	 */
	public double getCost() {
		return this.cost;
	}

	/**
	 * Set the book's cost.
	 * The book's cost can not be negative, and if it is set it to zero.
	 * 
	 * @param cost The book's cost in dollars.
	 */
	public void setCost(double cost) {
		if(cost >= 0)
			this.cost = cost;
		else
			this.cost = 0;
	}

	/**
	 * Get the book's title.
	 * 
	 * @return The book's title.
	 */
	public String getISBN() {
		return this.isbn;
	}

	/**
	 * Set the book's isbn.
	 * 
	 * @param isbn The book's isbn.
	 */
	public void setISBN(String isbn) {
		this.isbn = isbn;
	}
}
