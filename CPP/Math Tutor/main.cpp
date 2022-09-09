/*
Program     : Midterm Math Tutor
Description : This Program will ask the user to answer an equation
              given 3 tries. It includes addition and will keep a 
              running total of the user's score.
Author      : Thomas Marxsen
Date Written: 2021.10.20
*/

#include<iostream> //Needed for cin and cout
#include<string>   //Needed for at, size, and tolower Functions
#include<cstdlib>  //Needed for rand
#include<ctime>    //Needed to Seed Random With Time
#include<cmath>    //Needed for Round Function
#include<limits>   //Needed for numeric_limits for Error Handling
using namespace std;

int main(){
    string userName = "?";              //User's Inputs
    string gameStatus = "?";
    int userResponse = 0;

    int num1 = 0;                       //Values for Questions
    int num2 = 0;
    int correctAnswer = 0;

    double numCorrect = 0.00;           //Track User's Score
    double numIncorrect = 0.00;
    double userScore = 0.00;

    srand(time(0));                     //Seed for Rand

    //HEADER
    cout << endl;
    cout << "Welcome to The Best Math Tutor\n";
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    cout << endl;

    //USER'S NAME
    cout << "Please enter your name: ";
    getline(cin, userName);
    cout << endl;
    cout << "Welcome " << userName << " to the Best Math Tutor!\n";
    cout << endl;

    //RULES and Begin Game
    cout << "The rules of the game are as follows:\n";
    cout << "1) You have to answer random addition questions.\n";
    cout << "2) You will get three chances to answer each question correctly.\n";
    cout << "3) You can end the program after each question.\n";
    cout << endl;
    cout << "Now you can begin! Here is your first question!\n";

    //Set gameStatus to Enter Game
    gameStatus = "yes";

    //While Loop for Game
    while ((gameStatus == "yes") || (gameStatus == "y")) {

        cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";

        //Generating Random Numbers
        num1 = (rand() % 10 + 1);
        num2 = (rand() % 10 + 1);
        correctAnswer = num1 + num2;

        //For Loop of Questions Allowing Three Tries
        for (int i = 3; i > 0; i--) {

            cout << userName << " what is " << num1 << " + " << num2 << "? ";

            //While Loop for Error Handling
            while (!(cin >> userResponse)) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(),'\n');
                cout << "Invalid input! Please enter a number: ";
            }

            //If/Else to Test for the Correct Answer
            if (correctAnswer == userResponse) {

                //Switch for Correct Responses
                switch (i) {
                    case 3:
                        cout << "NICE! Right on your first try!\n";
                        numCorrect += 1;
                        break;
                    case 2:
                        cout << "WOWOWOWOWOWOW! You got it right on your second try!\n";
                        numCorrect += 1;
                        break;
                    case 1:
                        cout << "Dope! You got it right on your last try!\n";
                        numCorrect += 1;
                        break;
                    default:
                        cout << "You will be banished to the shadow realm for this atrocity.\n";
                        return -1;
                        break;
                }  //Closing Switch

                cout << endl;
                break;

            }  //Closing If Switch

            else {
                
                //Switch for Incorrect Responses
                switch (i) {
                    case 3:
                        cout << "Wow, WACK! You have two more attempts.\n";
                        break;
                    case 2:
                        cout << "Oh My! You have one attempt left.\n";
                        break;
                    case 1:
                        cout << "C'mon man, you can do better!\n";
                        cout << "The correct answer was: " << num1 << " + " << num2 << " = " << correctAnswer << endl;
                        numIncorrect += 1;
                        break;
                    default:
                        cout << "How did you even manage this.\n";
                        return -2;
                        break;
                }  //Closing Switch

                cout << endl;

            }  //Closing Else Switch

        }  //Closing For Question Loop

            //Set gameStatus to Enter While Loop
            gameStatus = '?';

            //Testing for an Invalid Response
            while (!((gameStatus == "yes") || (gameStatus == "y") || (gameStatus == "no") || (gameStatus == "n"))) {
                cout << "Would you like to continue? (yes/y or no/n): ";
                cin >> gameStatus;

                //For Loop to Set Response to Lower-case
                for (int j = 0; j <= gameStatus.size() - 1; j++) {
                gameStatus.at(j) = tolower(gameStatus.at(j));
                }
                
                if (!((gameStatus == "yes") || (gameStatus == "y") || (gameStatus == "no") || (gameStatus == "n"))) {
                cout << "Invalid Response.\n";
                }

            }  //Closing gameStatus While
        
    }  //Closing Game While

    //Determine User Percent Score
    userScore = round(100 * (numCorrect / (numCorrect + numIncorrect)));

    //Display Full Results
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    cout << endl;
    cout << "Best Math Tutor Results:\n";
    cout << "------------------------\n";
    cout << "Total Correct     = " << numCorrect << endl;
    cout << "Total Incorrect   = " << numIncorrect << endl;
    cout << "Your Score        = " << userScore << "%" << endl;
    cout << endl;
    
    //If to Give Feedback on Score
    if (userScore >= 95) {
        cout << "You are a math WIZARD!\n";
    }

    else if (userScore >= 90) {
        cout << "Wow! You're Great!\n";
    }

    else if (userScore >= 80) {
        cout << "You're pretty good at this math stuff!\n";
    }

    else if (userScore >= 70) {
        cout << "Looks like you need to play this game a lot more!\n";
    }

    else if (userScore < 70) {
        cout << "Looks like you really need more practice!\n";
    }

    //Closing
    cout << endl;
    cout << "Please come back soon " << userName << "!\n";
    cout << "The Game has Ended!\n";

    return 0;
}