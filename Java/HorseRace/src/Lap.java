public class Lap implements Runnable {
    // private int sleepTime;

    // Create an instance of Race to add a lap by passing the thread name
    public void addLap() {
        Race name = new Race(Thread.currentThread().getName());
    }

    @Override
    public void run() {

        runLap(); // Make the thread sleep to simulate running a lap
        addLap(); // Add the lap to the horse
    }

    // The thread will sleep for a random time
    private void runLap() {

        try {
            // sleepTime = (int) Math.floor(Math.random() * (1000 - 500 + 1) + 500);
            // System.out.println(Thread.currentThread().getName() + " sleeps for " +
            // sleepTime);

            // Thread sleeps for time between 1 and 0.5 seconds
            Thread.sleep((int) Math.floor(Math.random() * (1000 - 500 + 1) + 500));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

}
