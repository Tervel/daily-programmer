// Your mission is to create a stopwatch program. this program should 
// have start, stop, and lap options, and it should write out to a file 
// to be viewed later.

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class StopWatch {
    public static int mainMenu() {
        int selection;
        Scanner input = new Scanner(System.in);

        System.out.println("\nChoose an option:");
        System.out.println("1. Start");
        System.out.println("2. Stop");
        System.out.println("3. Lap");
        System.out.println("4. Display time\n");
        System.out.print(" >>  ");

        selection = input.nextInt();

        return selection;
    }

    public static void main(String[] args) throws Exception {
        long startTime = 0;
        ArrayList<String> lapTimes = new ArrayList<String>();
        
        while(true) {
            int choice = mainMenu();
            long elapsedTime = System.currentTimeMillis() - startTime;
            long elapsedMilli = elapsedTime / 100;
            long milliDisplay = elapsedTime % 60;
            long elapsedSeconds = elapsedTime / 1000;
            long secondsDisplay = elapsedSeconds % 60;
            long elapsedMinutes = elapsedSeconds / 60;

            switch (choice) {
                case 1:
                    startTime = System.currentTimeMillis();
                    break;
                case 2:
                    // Reset our time and all lap times
                    startTime = 0;
                    lapTimes.clear();
                    break;
                case 3:
                    // Lap: store elapsed time in array
                    lapTimes.add(String.format("Lap: %d:%d", secondsDisplay, milliDisplay));
                    break;
                case 4:
                    if (startTime != 0) {
                        System.out.printf("\nTime elapsed: %d:%d:%d\n", elapsedMinutes, secondsDisplay, milliDisplay);
                        for (int i = 0; i < lapTimes.size(); i++) {
                            System.out.println(lapTimes.get(i));
                        }
                    } else {
                        System.out.println("0");
                    }
                    break;
                default:
                    // null
                    break;
            }
        }
    }
}
