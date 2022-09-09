/*************************************************************
TODO:
Description: what this file for?
Pair Programmer #1 Name:
Pair Programmer #1 Replit:
Pair Programmer #2 Name:
Pair Programmer #2 Replit:
Date Written:
**************************************************************/

#include <iostream> // for cin & cout
#include <cstdlib>  // for srand & rand
#include <ctime>    // for getting the current time
#include <limits>   // for clearing the invalid input buffer

// TODO: what include do you need for working with vectors?

/* TODO: For Part 2 of this Assignment
You will need to include ONLY the header file like this:
#include "high_low.h"
do NOT also include the high_low.cpp
*/

using namespace std;

/*************************************************************
The main function keeps the program running as long as the user
wants to continue the game.
**************************************************************/
int main()
{

    // TODO: declare a vector storing int called rounds
    int computer = 0;	// the random number the computer generated for each round
    int human = 0; 		// the number the human is guessing
    int attempts = 0;	// attempts per round
    int average = 0;	// used for calculating the user's average

	// the Diff variables are used to determine if the human is
	// getting closer or futher away from the computer's number
    int currentDiff = 0;
    int previousDiff = 0;

    string yesNo = ""; 		 // used to validate y/n input
    bool keepPlaying = true; // set to false when they want to quit

	// make the random function more random by seeding it with current time
    srand(time(0)); 

    cout << "High Low Game!" << endl;
    cout << "==============" << endl;
    cout << endl;
    cout << "Where the human has to guess what the computer is thinking." << endl;
    cout << endl;
    cout << "======================" << endl;
    cout << "Within   5 = Very Hot" << endl;
    cout << "Within  10 = Hot" << endl;
    cout << "Within  50 = Warm" << endl;
    cout << "Within  60 = Cool" << endl;
    cout << "Within  80 = Cold" << endl;
    cout << "Within 100 = Very Cold" << endl;
    cout << "======================" << endl;
    cout << endl;
    cout << "Now let the fun begin...." << endl;
    cout << endl;

	// this loop keeps the game running until the human answer "no" to keep playing prompt
    while (keepPlaying) { 

		/* 
		for each new round do the following:
		reset the attempt counter 
		generate a new random number
		reset previousDiff back to -1 so we know when it's the human's first attempt for a new round
		*/
        attempts = 0; 
        computer = rand() % 100 + 1;
        previousDiff = -1;
		
        cout << "=================================================================" << endl;
        cout << "Guess what number am I thinking between 1-100 or enter 0 to quit." << endl;
        cout << "=================================================================" << endl;

		// this loop keep the round looping until the human guesses the correct number
        while (true){ 
            attempts++;

            cout << "=> "; // prompt the user for input
			
			// while loop to keep the program from ending on non-numeric data
            while (!(cin >> human)) { 									// if there is an error trying to get a numeric value
                cin.clear(); 											// clear the error
                cin.ignore(numeric_limits<streamsize>::max(),'\n'); 	// clear the data in the input buffer
                cout << "Invalid input! Please try again..." << endl;
                cout << "=> ";
            } // end of while loop for getting valid numeric input

			// how far away is the human from the computer's random number
			// use abs to avoid negative numbers so both 40 and 60 would be 10 away from 50
            currentDiff = abs(computer - human); 

			// human can enter 0 if they want to quit guessing in the middle of a round
            if (human == 0){ 
                cout << "I can't believe you are giving up :(" << endl;
                break;
            } else if (human == computer) {
                cout << "Correct!" << endl;
                break;
            }

			// -1 is used to determine if it's the human's first guess for the round
            if(previousDiff == -1) { 
                if (currentDiff < 50) {
                    cout << "You are off to a good start ";
                } else {
                    cout << "Looks like you might be here for a while ";
                }
            } else {
                if (currentDiff < previousDiff) {
                    cout << "You are getting closer ";
                } else {
                    cout << "You are getting further away ";
                }
            }

            if (currentDiff < 5)
                cout << "(very hot = within 5)" << endl;
            else if (currentDiff < 10)
                cout << "(hot = within 10)" << endl;
            else if (currentDiff < 50)
                cout << "(warm = within 50)" << endl;
            else if (currentDiff < 60)
                cout << "(cool = within 60)" << endl;
            else if (currentDiff < 80)
                cout << "(cold = within 80)" << endl;
            else
                cout << "(very cold = within 100)" << endl;

            previousDiff = currentDiff;

        } // keepGuessing


		// if the human did NOT give up before getting it correct
        if (human != 0){ 
            //TODO: add the number of attempts to the end of the vector
        }

        cout << endl;
		
		// keep looping until the user enters a word that starts with a y or n
        while (true){ 

            cout << "Do you want to play again? (y=yes, n=no): ";
            cin >> yesNo;

            if (tolower(yesNo.at(0)) == 'y'){
                keepPlaying = true;
                break;
            } else if (tolower(yesNo.at(0)) == 'n') {
                keepPlaying = false;
                break;
            } else {
                cout << "Invalid input!" << endl;
            }

        } // end of do you want to cont while loop
		
        cout << endl;

    } // keepPlaying


    /* TODO: Display the following report:

        ===================================
        Round #1 took you 6 guesses
        Round #2 took you 4 guesses
        ===================================
        On average, it took you 5 guesses.

    Pseudocode:
    ------------------------------------------------------------------
    set attempts to zero
    for loop based on the size of the vector
        display the round attempts
        add to running total of attempts
    end of for loop
    calculate the average based on attempts and the size of the vector
    display the user's average
    */

    cout << "I hope you want to play again soon." << endl;

    return 0;
}
