import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class StopWatch {
	public static int mainMenu() {
		int selection;
		Scanner input = new Scanner(System.in);

		System.out.println("Choose an option:");
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
		

		while(true) {
			int choice = mainMenu();
			long elapsedTime = System.currentTimeMillis() - startTime;
			long elapsedMilli = elapsedTime / 100;
			long elapsedSeconds = elapsedTime / 1000;
			long secondsDisplay = elapsedSeconds % 60;
			long elapsedMinutes = elapsedSeconds / 60;

			switch (choice) {
				case 1:
					startTime = System.currentTimeMillis();
					break;
				case 2:
					break;
				case 3:
					// Lap: store elapsed time in array
					break;
				case 4:
					System.out.printf("\nTime elapsed: %d:%d:%d\n", elapsedMinutes, elapsedSeconds, elapsedMilli);
					break;
				default:
					// null
					break;
			}
		}
	}
}
