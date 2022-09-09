package library.inventory;

/** 
 * Enum is a special "class" that represents a group of constants 
 * Only three valid Statuses,which are CIRCULATING, REFERENCE, and RESERVE.
 * 
 * @author Thomas Marxsen
 * @version 1.0
 * @since 2022.03.23
 */
public enum Status {
	/**
	 * Status for circulating inventory.
	 */
	CIRCULATING,

	/**
	 * Status for reference inventory.
	 */
	REFERENCE,

	/**
	 * Status for reserve inventory.
	 */
	RESERVE
}