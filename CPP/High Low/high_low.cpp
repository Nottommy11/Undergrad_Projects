/*************************************************************
TODO:
Description: Contains functions for use with High Low game
Pair Programmer #1 Name: Thomas Marxsen
Pair Programmer #1 Replit: https://replit.com/join/dbqvrgoloa-nottommy11
Pair Programmer #2 Name: Jadyn Keller
Pair Programmer #2 Replit: https://replit.com/join/umoxnknugd-jakell10
Date Written: 11/17/2021
**************************************************************/
#include <iostream> //for cin & cout
#include <vector>   //for vectors
#include <limits>   //for clearing the invalid input buffer

using namespace std;

/*************************************************************
The DisplayHeading function is used to display the program
title, and instructions.
**************************************************************/
void DisplayHeading(){
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
}

/*************************************************************
The GetNumber function will display the => prompt
and keep looping until the user enters a valid numeric input.
This function will return a valid number value
**************************************************************/
int GetNumber(){
  int human = 0;

  cout << "=> ";		// prompt the user for input

  while (!(cin >> human)) {
// if there is an error trying to get a numeric value
    cin.clear();
// clear the error
    cin.ignore(numeric_limits<streamsize>::max(),'\n');		// clear the data in the input buffer
    cout << "Invalid input! Please try again..." << endl;
    cout << "=> ";
  } // end of while loop for getting valid numeric input
  return human;
}

/*************************************************************
The DisplayHighLowMsg will display if they are getting closer
or further away.  If it's the user's first attempt, it will
display if they are off to a good start or not.
**************************************************************/
void DisplayHighLowMsg(int previousDiff, int currentDiff){
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
}

/*************************************************************
The DisplayTemp function will display if they are very hot,
hot, warm, cool, cold, or very cold.
**************************************************************/
void DisplayTemp(int currentDiff){
  int previousDiff = -1;
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
}

/*************************************************************
The PlayAgain function will ask the user if they want to play
again.  It will keep looping until the user enters a y/n.
The function will return true if the user wants to continue or
return false if the user wants to quit.
**************************************************************/
bool PlayAgain(){
  
  string yesNo = ""; // used to validate y/n input
  bool keepPlaying = true;

		// keep looping until the user enters a word that starts with a y or n
    while (true){
      cout << "Do you want to play again? (y=yes, n=no): ";
      cin >> yesNo;

      if (tolower(yesNo.at(0)) == 'y'){
          return true;
      } else if (tolower(yesNo.at(0)) == 'n') {
          return false;
      } else {
          cout << "Invalid input!" << endl;
      }
    } // end of do you want to cont while loop
}

/*************************************************************
The DisplayResults function will display each round of the
game and how many guesses it took the human to guess the
correct number.  It will then calculate and display the
average.
**************************************************************/
void DisplayResults(const vector<int>& rounds){
  int roundNum = 1;
  int average = 0;

  if (rounds.size() > 0){
    cout << "===================================\n";
    
    for (int i = 0; i < rounds.size(); i++) {
      cout << "Round #" << roundNum++ << " took you " << rounds.at(i) << " guesses\n";
    }
  
    cout << "===================================\n";

    for (int i = 0; i < rounds.size(); i++) {
      average += rounds.at(i);
    }
    
    average /= rounds.size();

    cout << endl;
    cout << "On average, it took you " << average << " guesses.\n";
  }
}