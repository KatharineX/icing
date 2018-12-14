import java.io.IOException;
import java.io.File;
import java.util.Scanner;
import java.io.*;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.*;

public class MazeGame {
    static int LifeCount;
    static int GoldCounter;
    static int StepCounter;
    static int currentYIndex;
    static int currentXIndex;
    static int NumberOfLives;
    static int AmountOfGold;
    static int rows;
    static int array_length;
    static ArrayList<String> list;
    static int x;
    static int y;
    static String FileName;
    static String nextra;
    static String userBInput;
    static int index;
    static boolean counts;
    static int nums;
    static int setterdos;
    static int setteruno;
    static String maction;
    static String command;
    static String[] User_inp;
    static Scanner userInput;
    static String toSave;

    public static void initialiseGame(String configFileName) throws IOException {
        File newFile = new File(configFileName);
        Scanner b = new Scanner(newFile);
        String[] arr = b.nextLine().split(" ");
        array_length = arr.length;

        setteruno = 0;
        setterdos = 0;
        x = 0;
        y = 0;
        counts = false;
        AmountOfGold = 0;
        currentXIndex = 0;
        currentYIndex = 0;
        maction = "hell";
        command = "bell";
        FileName = "hall";
        nextra = "ball";
        toSave = "";
        LifeCount = Integer.parseInt(arr[0]);
        StepCounter = Integer.parseInt(arr[1]);
        GoldCounter = Integer.parseInt(arr[2]);
        rows = Integer.parseInt(arr[3]);
        // System.out.print(NumberOfLives+""+ NumberOfSteps+""+ AmountOfGold);

        list = new ArrayList<String>(0);

        while (b.hasNextLine()) {
            String[] chars = b.nextLine().split("");

            for (int i = 0; i < chars.length; i++) {
                String chams = chars[i];
                list.add(chams);
            }
        }
    }

    // TO ACTION
    public static void saveGame(String toFileName) throws IOException {

        PrintWriter writer = new PrintWriter(new FileWriter(toFileName));
        writer.write(numberOfLives() + " " + numberOfStepsRemaining() + " " + amountOfGold() + " " + rows);
        writer.write("\n");
		
        String twoDmArr[][] = new String[rows][list.size() / rows];
        String[] stockArr = new String[list.size()];

        for (int k = 0; k < list.size(); k++) {
            stockArr[k] = (list.get(k));
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < (list.size() / rows); j++) {
                twoDmArr[i][j] = stockArr[(i*(list.size()/rows)) + j];
            }
        }

        for (String[] row : twoDmArr) {
            for (String i : row) {
                writer.write(i);
            }
            writer.write("\n");
        }
		writer.close();
		System.out.println("You have successfully saved the current game configuration to '"+ toFileName + "'");
    }

    public static int getCurrentXPosition() {

        index = list.indexOf("&");
        currentXIndex = index % (list.size() / rows);
        return currentXIndex;
    }

    public static int getCurrentYPosition() {
        index = list.indexOf("&");
        currentYIndex = index / (list.size() / rows);
        return currentYIndex;

    }

    public static int numberOfLives() {
        return LifeCount;
    }

    public static int numberOfStepsRemaining() {
        return StepCounter;
    }

    public static int amountOfGold() {
        return AmountOfGold;
    }

    public static boolean isMazeCompleted() {
         int winner = list.indexOf('@');

        counts = false;
        if (list.get(y*(list.size()/rows) + x).equals("@")&& winner == (y*(list.size()/rows)+x)) {
            counts = true;
        }
        return counts;
    }

    public static boolean isGameEnd() {
        counts = false;

        if (StepCounter <= 0 || LifeCount <= 0 || isMazeCompleted()) {
            counts = true;
        }
        return counts;
    }

    public static boolean isValidCoordinates(int x, int y) {
        counts = true;
        if (x > ((list.size() / rows) - 1) || x < 0 || y > (rows - 1) || y < 0) {
            counts = false;
            // StepCounter -= 1;
            // LifeCount -= 1;
        }
        return counts;
    }

    public static boolean canMoveTo(int x, int y) {
        counts = true;

        if (isGameEnd() || isValidCoordinates(x, y) == false || list.get(y * (list.size() / rows) + x).equals("#")) {
            counts = false;
        }
        return counts;
    }

    public static void moveTo(int x, int y) {
		
	
        if (isGameEnd() == false && canMoveTo(x, y) && isValidCoordinates(x, y)) {
            String val = list.get(y*(list.size()/rows) +x);

            try {

                System.out.println("Moved to (" + x + ", " + y + ").");
                StepCounter -= 1;
                if (Integer.parseInt(val) == (Integer.parseInt(val))) {
                    AmountOfGold += Integer.parseInt(val);
                    System.out.println("Plus " + Integer.parseInt(val) + " gold.");
                }
            } catch (NumberFormatException r) {

            }
            setteruno = (y * (list.size() / rows) + x);
			setterdos = (getCurrentYPosition()) * (list.size() / rows) + (getCurrentXPosition());


            if(list.get(y * (list.size() / rows) + x).equals("@")){
               System.out.println("Congratulations! You completed the maze!");
            System.out.println("Your final status is:");
            MazeGame.printStatus();
            }else{
				
				list.set(setteruno, "&");
            list.set(setterdos, ".");

			}
            
        } else {
			   LifeCount -= 1;
			StepCounter -= 1;
            System.out.println("Invalid move. One life lost.");
         
        }
    }

    public static void printHelp() {
        System.out.println("Usage: You can type one of the following commands.");
        System.out.println("help         Print this help message.");
        System.out.println("board        Print the current board.");
        System.out.println("status       Print the current status.");
        System.out.println("left         Move the player 1 square to the left.");
        System.out.println("right        Move the player 1 square to the right.");
        System.out.println("up           Move the player 1 square up.");
        System.out.println("down         Move the player 1 square down.");
        System.out.println("save <file>  Save the current game configuration to the given file.");
    }

    public static void printStatus() {
        System.out.println("Number of live(s): " + LifeCount);
        System.out.println("Number of step(s) remaining: " + numberOfStepsRemaining());
        System.out.println("Amount of gold: " + GoldCounter);
    }

    public static void printBoard() {
        String twoDmArr[][] = new String[rows][list.size() / rows];
        String[] stockArr = new String[list.size()];

        for (int k = 0; k < list.size(); k++) {
            stockArr[k] = (list.get(k));
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < (list.size() / rows); j++) {
                twoDmArr[i][j] = stockArr[(i * (list.size() / rows)) + j];
            }
        }

        for (String[] row : twoDmArr) {
            for (String i : row) {
                System.out.print(i);
            }
            System.out.println();
        }

    }

    public static void performAction(String action) throws IllegalArgumentException {

        x = getCurrentXPosition();
        y = getCurrentYPosition();
        if (isMazeCompleted()) {
            System.out.println("Congratulations! You completed the maze!");
            System.out.println("Your final status is:");
            MazeGame.printStatus();
        } else if (isGameEnd()) {

            if (StepCounter == 0) {
                // System.out.println("Invalid move. One life lost.");
                System.out.println("Oh no! You have no steps left.");
                System.out.println("Better luck next time!");

            } else if (LifeCount == 0) {
                // System.out.println("Number of live(s): " + LifeCount+"'");
                System.out.println("Oh no! You have no lives left.");
                System.out.println("Better luck next time!");
            }

            System.out.println("You did not complete the game.");

        } else {
		}

            if (action.equals("help")) {
                printHelp();

            } else if (action.equals("board")) {
                printBoard();

            } else if (action == null) {
               // System.out.println("You did not complete the game.");

            } else if (action == ""){} 
			
			else if (action.equals("status")) {
                printStatus();

            } else if (action.equals("left")) {
                if (canMoveTo(x - 1, y) && isValidCoordinates(x - 1, y)) {
                    moveTo(x - 1, y);
					
                } else {
					LifeCount -= 1;
                    System.out.println("Invalid move. One life lost.");
                    
                }
            } else if (action.equals("right")) {
                if (canMoveTo(x + 1, y) && isValidCoordinates(x + 1, y)) {
                    moveTo(x + 1, y);

                } else {
                    System.out.println("Invalid move. One life lost.");
                    LifeCount -= 1;
                }
            } else if (action.equals("up")) {
                if (canMoveTo(x, y - 1) && isValidCoordinates(x, y - 1)) {
                    moveTo(x, y - 1);

                } else {
                    System.out.println("Invalid move. One life lost.");
                    LifeCount -= 1;
                }
            } else if (action.equals("down")) {
                if (canMoveTo(x, y + 1) && isValidCoordinates(x, y + 1)) {
                    moveTo(x, 1 + y);

                } else {
                    System.out.println("Invalid move. One life lost.");
                    LifeCount -= 1;
                }

            } else if (action.equals("save")) {
                if (User_inp.length > 2 || User_inp.length == 1) {
                    System.out.println("Error: Could not save current game configuration to '" + User_inp[1] + "'.");
                   // System.out.println("To find the list of valid commands, please type 'help'.");
                } else if (User_inp.length == 2) {
                    try {
                        saveGame(toSave);
                    } catch (IOException o) {
						
                       // System.out.println("fek");
                       // System.out.println("To find the list of valid commands, please type 'help'.");
                    }
                }

            } //else {
				
              //  System.out.print("Error: Could not find command '" + nextra +  "'.");
                
            //}
		
		try {
                userInput = new Scanner(System.in);
                nextra = userInput.next();
                User_inp = nextra.split(" ");
                command = User_inp[0];
                // System.out.print(command);
                maction = command.toLowerCase();
	
			performAction(maction);
			
		
		}
		catch (Exception s) {

            }

    }

    public static void main(String[] args) {

        try {
            if (args.length > 1) {
                System.out.println("Error: Too many arguments given. Expected 1 argument, found " + args.length + '.');
                System.out.println("Usage: MazeGame [<game configuration file>|DEFAULT]");
            } else if (args.length == 0) {
                System.out.println("Error: Too few arguments given. Expected 1 argument, found 0.");
                System.out.println("Usage: MazeGame [<game configuration file>|DEFAULT]");
            } else if (args.length == 1) {
                FileName = args[0];
                initialiseGame(FileName);
                try {

                    userInput = new Scanner(System.in);
                    nextra = userInput.next();
                    User_inp = nextra.split(" ");
                    command = User_inp[0];
					if (maction.equals("save")) {
                        toSave = User_inp[1];
                        performAction(maction);
                    } else {
                        performAction(maction);
                    }
                   
                } catch (Exception p) {
                    System.out.println("You did not complete the game.");
                }
				 	maction = command.toLowerCase();

                    

            } else {
                System.out.println("Error could not load the game file from '" + FileName + "'");
            }
        } catch (IOException e) {
            System.out.println("Error: Could not load the game configuration from '" + FileName + "'.");
        }
    }
}
