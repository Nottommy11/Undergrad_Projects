/*************************************************************
Program that allows many players to join/save/load a game of 21
Programmer: Thomas Marxsen
Date Written: 2021.12.12
**************************************************************/
#include <iostream>     // for cin, cout, fixed, showpoint
#include <string>       // for strings
#include <cstdlib>      // for srand and rand
#include <ctime>        // for seeding the current time to srand
#include <vector>       // for vectors
#include <iomanip>      // for setw, setprecision
#include <fstream>      // for reading and writing to files
#include <exception>    // for throw, try, catch handling

#include "game21.h"     // header file with function prototypes
#include "game21.cpp"   // VS Code didn't want to work without the .cpp file included

using namespace std;

/*************************************************************
The main function that keeps the game running
**************************************************************/
int main()
{
    int dealerCardsTotal = 0;   // the total of all cards dealt to the dealer
    int highestHand = 0;        // no there is no highest hand then all players exceeded 21 (dealer wins)
    int playersWithCash = 0;    // keep track of how many players still have money

    string playerCards = "?";   // used with string stream storing a list of a player's cards

    vector<string> playerNames;     // stores all the player's names
    vector<int> playerCardsTotal;   // stores a total of each player's cards (reset for each round)
    vector<double> playerCash;      // stores a player's cash winnings value
    vector<double> playerBets;      // stores the players current bet (reset for each round)

    bool keepPlaying = true;    // used to keep the game running

    bool canLoad = true;        //Can load a previous game if file is found

    srand(time(0));             // make the random function more random by seeding the current time

    DisplayGameIntro();

    //Load a previous game file
    try {
        LoadGame(playerNames, playerCash);
    } catch (runtime_error& excpt) {
        cout << excpt.what() << endl;
        cout << "Program did NOT end normally" << endl;
        canLoad = false;
    }

    //Display the previous game file, if any
    if (canLoad == true) {
        DisplayPreviousGame(playerNames, playerCash);
    }

    if  (playerNames.size() == 0) {
        GetPlayerNames(playerNames);
    }

    if (playerNames.size() == 0){
        cout << endl;
        cout << "=========================================================================" << endl;
        cout << "  Game over! No players :(" << endl;
        cout << "=========================================================================" << endl;
        return(0);
    }

    // start each player off with $1
    for (unsigned int i = 0; i < playerNames.size(); i++){
        playerCash.push_back(1.0);
    }

    cout << endl;
    cout << "=========================================================================" << endl;
    cout << "Starting game..." << endl;
    cout << "=========================================================================" << endl;
    cout << endl;

    while (keepPlaying){

        highestHand = DealPlayers(playerNames, playerBets, playerCash, playerCardsTotal);

        /*
        if highestHand is zero this means all players exceeded the 21 limit
        which means no players are still playing the current round
        which means there is no need to deal cards to the dealer because
        the dealer automatically wins
        */
        if (highestHand > 0){
            dealerCardsTotal = DealDealer(highestHand);
        } else {
            dealerCardsTotal = 21; // make the dealer a winner if all players exceeded 21
        }

        DisplayWinningPlayers(playerNames, playerBets, playerCash, playerCardsTotal, dealerCardsTotal);

        playersWithCash = RoundSummary(playerNames, playerCash);

        cout << "===========================================" << endl;
        if(playersWithCash == 0){ // if no players have cash left then the game will end
            cout << "All players are out of the game." << endl << endl;
            break; // break out of the keep playing while loop
        } else {
            /*
            ConfirmPrompt will return true or false which will automatically
            control if the game keeps looping
            */
            keepPlaying = ConfirmPrompt("Do you want to play again");
        }
        cout << "===========================================" << endl;
        cout << endl;
    } // end of while keepPlaying

    try {
        SaveGame(playerNames, playerCash);
    } catch (runtime_error& excpt) {
        cout << excpt.what() << endl;
        cout << "Program did NOT end normally" << endl;
    }
    
    cout << endl;
    cout << "=========================================================================" << endl;
    cout << "Game Over :(" << endl;
    cout << "=========================================================================" << endl;

    return 0;
}
