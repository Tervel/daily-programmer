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
		System.out.println("3. Lap\n");
		System.out.print(" >>  ");

		selection = input.nextInt();

		return selection;
	}

	public static void main(String[] args) throws Exception {
		int choice = mainMenu();

		switch (choice) {
			case 1:
				// Start
				break;
			case 2:
				// Stop
				break;
			case 3:
				// Lap
				break;
		}
	}
}
