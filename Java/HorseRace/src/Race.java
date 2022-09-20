import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/*
 * Thomas Marxsen
 * Daniel Cancino
 * Esteban Cancino
 * Faith Nunn
 */
public class Race {

    // Tracks the number of laps for each horse
    static int loafLaps = 0;
    static int breadLaps = 0;
    static int chipsLaps = 0;
    static int eggsLaps = 0;
    static int milkLaps = 0;

    // Assigns a thread to each horse
    private String loafThread = "pool-1-thread-1";
    private String breadThread = "pool-1-thread-2";
    private String chipsThread = "pool-1-thread-3";
    private String eggsThread = "pool-1-thread-4";
    private String milkThread = "pool-1-thread-5";

    // List of the places the horses got
    static List<String> places = new ArrayList<>();

    // Adds laps
    public Race(String name) {
        if (name.equals(loafThread)) { // Check if current thread is the horse
            loafLaps += 1; // Adds a lap
            // System.out.println("Loaf Lap: " + loafLaps);
            if (loafLaps == 5) { // If laps equals 5, horse is done
                // System.out.println("Loaf is done!");
                places.add("Loaf"); // Add the horse to the places list
            }
        } else if (name.equals(breadThread)) {
            breadLaps += 1;
            // System.out.println("Bread Lap: " + breadLaps);
            if (breadLaps == 5) {
                // System.out.println("Bread is done!");
                places.add("Bread");
            }
        } else if (name.equals(chipsThread)) {
            chipsLaps += 1;
            // System.out.println("Chips Lap: " + chipsLaps);
            if (chipsLaps == 5) {
                // System.out.println("Chips is done!");
                places.add("Chips");
            }
        } else if (name.equals(eggsThread)) {
            eggsLaps += 1;
            // System.out.println("Eggs Lap: " + eggsLaps);
            if (eggsLaps == 5) {
                // System.out.println("Eggs is done!");
                places.add("Eggs");
            }
        } else if (name.equals(milkThread)) {
            milkLaps += 1;
            // System.out.println("Milk Lap: " + milkLaps);
            if (milkLaps == 5) {
                // System.out.println("Milk is done!");
                places.add("Milk");
            }
        }
    }

    // Pretty
    public static void spacer() {
        System.out.println();
        System.out.println("======================================");
        System.out.println();
    }

    public static void main(String[] args) throws Exception {

        // Create a pool of 5 threads
        ExecutorService executor = Executors.newFixedThreadPool(5); // Recycle threads

        spacer();
        System.out.println("Starting the Race!");
        spacer();

        // Create 30 processes for the threads to run
        for (int i = 1; i <= 30; i++) {
            Runnable processor = new Lap();
            executor.execute(processor);
        }

        // Shutdown the pool so the program can exit gracefully
        executor.shutdown();

        // Keeps main here until pool is shutdown
        while (!executor.isTerminated()) {
        }

        System.out.println("Race Complete!");
        spacer();

        // Print out the places
        for (int i = 0; i < 5; i++) {
            System.out.println("Place #" + (i + 1) + " goes to: " + places.get(i));
        }
        spacer();

    }
}
