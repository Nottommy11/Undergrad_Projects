/*************************************************************
Function file with all the Game 21's functions
Programmer: Thomas Marxsen
Date Written: 2021.12.12
**************************************************************/
#include <iostream>     // for cin, cout, fixed, showpoint
#include <string>       // for strings
#include <vector>       // for vectors
#include <sstream>      // for string streams
#include <iomanip>      // for setw, setprecision
#include <fstream>      // for reading and writing to files
#include <exception>    // for throw, try, catch handling
#include <cstdlib>      // for srand and rand

using namespace std;

// used for generating random numbers
const int NUM_CARDS = 10;

// file name where the previous game's players cash winnings
const string GAME21_FILE = "game21.txt";

/*************************************************************
The ConfirmPrompt function will ask the user a yes/no question.
It will keep looping until the user enters a y/n.
The function will return true if the user wants to continue or
return false if the user wants to quit.
**************************************************************/
bool ConfirmPrompt(const string prompt){

    string yesNo = "?";

    while (true){

        cout << prompt << "? (y=yes, n=no): ";
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
The DisplayGameIntro function displays the game's title
and rules.
**************************************************************/
void DisplayGameIntro(){
    cout << "=========================================================================" << endl;
    cout << "                        Welcome to Game 21" << endl;
    cout << "=========================================================================" << endl;
    cout << "The rules are simple!" << endl;
    cout << "  1. Each player is trying to get as close to 21 without going over." << endl;
    cout << "  2. Each player is ONLY trying to beat the dealer's hand." << endl;
    cout << "  3. The dealer will keep dealing himself cards" << endl;
    cout << "     until he beats all players hands or goes over 21." << endl;
    cout << "  4. Tie goes to the player, not the dealer." << endl;
    cout << "  5. Each player gets dealt two cards between 1 - 10." << endl;
    cout << "  6. The player then can choose to receive additional cards." << endl;
    cout << "  7. Each player starts with $1.00" << endl;
    cout << "  8. Default bet is 25 cents, but the player can double it after holding." << endl;
    cout << "  9. Winner is the last person with cash, not including the dealer." << endl;
    cout << endl;
    cout << "=========================================================================" << endl;
    cout << endl;
}

/*************************************************************
This function will search for a previous game in a save file
**************************************************************/
void LoadGame(vector<string>& playerNames,
              vector<double>& playerCash) {

    string inPlayerNames = "?";
    double inPlayerCash = 0;

    ifstream inFS; // Input stream file handle

	// make sure the vectors are empty before loading the file
    playerNames.clear();
    playerCash.clear();

    inFS.open(GAME21_FILE);

    if (!inFS.is_open()) {
        throw runtime_error("Could not open file " + GAME21_FILE + " for reading");
    }

    while (inFS >> inPlayerNames >> inPlayerCash) {
        playerNames.push_back(inPlayerNames);
        playerCash.push_back(inPlayerCash);
    }

    if (!inFS.eof()) {
        throw runtime_error("Something went wrong with reading the " + GAME21_FILE + " file.");
    }

    // Done with file, so close it
    inFS.close();
}

/***********************************************************
This function is used to display the previous game and ask 
the user if they want to load it
***********************************************************/
void DisplayPreviousGame(vector<string>& playerNames,
                         vector<double>& playerCash) {

    string inPlayerNames = "?";
    double inPlayerCash = 0;
    int colSize = 0;
    string playName = "?";

    cout << setfill(' ');
    cout << fixed << showpoint << setprecision(2);

    cout << "Previous Game Winnings" << endl << endl;

    for(int i = 0; i < playerNames.size(); i++) {
        playName = playerNames.at(i);
        colSize = 35 - playName.size();                 //Setting column size minus the player's name size

        cout << "  " << playerNames.at(i) << setw(colSize) << left << "'s Total Winnings was" << setw(5) << right << "$" << playerCash.at(i) << endl;
    }

    cout << endl;
    cout << "=========================================================================" << endl << endl;

    if (!ConfirmPrompt("Do you want to load your previous game")) {
        cout << "Game not loaded" << endl;

        // make sure the vectors are empty if not loading file
        playerNames.clear();
        playerCash.clear();

        return;
    }

    cout << "Game Loaded!" << endl;
}

/*************************************************************
The GetPlayerNames function gets all the player's names :)
**************************************************************/
void GetPlayerNames(vector<string>& playerNames){

    string playerName = "?";    // used to get each player's name

    cout << endl;
    cout << "=========================================================================" << endl << endl;
    cout << "Now lets get this game setup.  Who is all playing?" << endl;
    cout << "  Please enter a player's name or enter 'done' when finished." << endl;
    cout << endl;

    // while loop for getting all player's names
    while (true) {
        cout << "  Enter the player's first name (without spaces): ";
        cin >> playerName;

        if (playerName == ""){
            cout << "  Error! No name entered. Please try again, or enter 'done' when finished." << endl;
            continue;
        }

        if (playerName == "done") {
            break;
        }

        playerNames.push_back(playerName);  // store the player's name
    }
}

/*************************************************************
The DealPlayers function will deal cards to all players
and return the highest hand value
**************************************************************/
int DealPlayers(const vector<string>& playerNames,
                vector<double>& playerBets,
                const vector<double>& playerCash,
                vector<int>& playerCardsTotal){

    int randNum = 0;            // storing the current random number
    ostringstream cardsOSS;     // used to store a list of the current player's cards as they get dealt

    // at the start of each round reset the following values
    int highestHand = 0;        // this is used to determine when to stop dealing cards to the dealer
    playerCardsTotal.clear();   // delete all player's card total - vector is empty
    playerBets.clear();         // delete all player's bets - vector is empty

    // for loop to deal cards to each player
    for (unsigned int i = 0; i < playerNames.size(); i++){

        playerCardsTotal.push_back(0);  // set the current's player hand total to zero
        playerBets.push_back(0.0);      // set the current's bet to zero

        // if the player has no cash, then skip this player
        if (playerCash.at(i) < 0.25)
            continue;

        // the cardesOOS string stream is used to store what cards are dealt to the current player
        cardsOSS.str("");   // clear all cards
        cardsOSS.clear();   // so that subsequent extractions start from the beginning of the string

        cout << "Dealing to " << playerNames.at(i) << endl;

        randNum = (rand() % NUM_CARDS) + 1; // first player's card
        playerCardsTotal.at(i) += randNum;  // add the card value to the player's total
        cardsOSS << randNum << " ";         // add the card to the list of cards

        randNum = (rand() % NUM_CARDS) + 1; // second player's card
        playerCardsTotal.at(i) += randNum;  // add the card value to the player's total
        cardsOSS << randNum << " ";         // add the card to the list of cards

        cout << "  Cards: " << cardsOSS.str() << endl; // display the player's first two cards

        // keep looping while the player wants another card
        while (true) {

            // if the player does NOT want another card
            if (!ConfirmPrompt("  Do you want another card")) {

                cout << "  " << playerNames.at(i) << " holds at " << playerCardsTotal.at(i) << endl;

                //only ask the player if they want to double their bet IF they have more than 25 cents
                if (playerCash.at(i) >= 0.5 && ConfirmPrompt("  Do you want to double your 25 cent bet")){
                    playerBets.at(i) = 0.5;
                } else {
                    playerBets.at(i) = 0.25;
                }

                /*
                highestHand is used to determine how many cards will be dealt to the dealer
                because the dealer will keep dealing himself cards until he beats all player's hands
                or when the dealer exceeds 21
                */
                if (playerCardsTotal.at(i) > highestHand) {
                    highestHand = playerCardsTotal.at(i);
                }

                break;  // break out of the while loop because the player doesn't want any more cards
            }

            randNum = (rand() % NUM_CARDS) + 1; // randomly generate another card's value
            playerCardsTotal.at(i) += randNum;  // add the card to the player's total
            cardsOSS << randNum << " ";         // add the card to the list of player's cards

            cout << "  Cards: " << cardsOSS.str() << endl; // display the current list of the player's cards

            /*
            if the player exceeds 21 then set the player's card total to -1
            indicating they are knock out of the current round
            */
            if (playerCardsTotal.at(i) > 21){
                playerBets.at(i) = 0.25; // the player will lose the default bet value

                playerCardsTotal.at(i) = -1;
                cout << "  Sorry, " << playerNames.at(i) << "\'s hand exceeded 21" << endl;
                break; // do not deal the player any more cards
            }
        } // end dealing cards to the current player

        cout << endl;

    } // end of for looping through players

    return highestHand;
}

/*************************************************************
The DealDealer function will deal the dealer cards and
return the deal's cards total
**************************************************************/
int DealDealer(int highestHand){
    int randNum = 0;            // storing the current random number
    int dealerCardsTotal = 0;   // the dealer's card total for each round
    ostringstream cardsOSS;     // used to store a list of the current player's cards as they get dealt

    cout << "Dealing to the dealer" << endl;

    // the cardesOOS string stream is used to store what cards are dealt to the current player
    cardsOSS.str("");       // clear all cards
    cardsOSS.clear();       // so that subsequent extractions start from the beginning of the string

    /*
    only enter this while loop if there is at least one player that is still playing this round
    meaning they did not exceed the 21 limit
    */
    while (true && highestHand > 0){
        randNum = (rand() % NUM_CARDS) + 1; // deal a card to the dealer
        dealerCardsTotal += randNum;        // add the card value to the dealer's total
        cardsOSS << randNum << " ";         // add the card to the list of dealer's cards

        // if the dealer exceeds 21
        if (dealerCardsTotal > 21){
            dealerCardsTotal = 0;
            cout << "  Cards: " << cardsOSS.str() << endl;  // display the dealer's cards
            cout << "  Dealer\'s hand exceeded 21" << endl;
            cout << endl;
            break;
        // done dealing to the dealer if they reach 21 OR beat all player's hands
        } else if (dealerCardsTotal == 21 || dealerCardsTotal > highestHand){
            cout << "  Cards: " << cardsOSS.str() << endl;  // display the dealer's cards
            cout << "  Dealer holds at " << dealerCardsTotal << endl;
            break;
        }
    }

    return dealerCardsTotal;

}

/*************************************************************
The DisplayWinningPlayers will display all the players who
won the current round.
**************************************************************/
void DisplayWinningPlayers(const vector<string>&playerNames,
                           const vector<double>& playerBets,
                           vector<double>& playerCash,
                           const vector<int>& playerCardsTotal,
                           const int dealerCardsTotal){

    int totalWinners = 0;       // if no winners then the dealer is the winner

    cout << endl;
    cout << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" << endl;

    // display which players bet the dealer's hand
    for (unsigned int i = 0; i < playerNames.size(); i++){
        // skip the players that are out of money
        if (playerCash.at(i) < 0.25){
            continue;
        }

        /*
        if the player beat the dealer's total
        then display that the player won
        and increase their cash value by the player's beat
        */
        if (playerCardsTotal.at(i) >= dealerCardsTotal){
            totalWinners++; // if there are no winners the dealer automatically wins
            playerCash.at(i) += playerBets.at(i);
            cout << playerNames.at(i) << " is a winner!" << endl;

        // else lower the player's cash value by the player's beat
        } else {
            playerCash.at(i) -= playerBets.at(i);
        }
    }

    // if no player won then the dealer automatically wins
    if (totalWinners == 0){
        cout << "Dealer is a winner!" << endl;
    }

    cout << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" << endl;
    cout << endl;
}

/*************************************************************
The RoundSummary will display the Player's cash balance
and return how many players with a balance (still in the game)
**************************************************************/
int RoundSummary(const vector<string>& playerNames,
                 const vector<double>& playerCash){

    int playersWithCash = 0;  // used to keep track if no player has cash left then the game will end

    cout << "End of Round Summary" << endl;
    cout << "====================" << endl;

    // at the end of the round, display each player's cash value
    for (unsigned int i = 0; i < playerNames.size(); i++){
        if (playerCash.at(i) < 0.25){
            cout << playerNames.at(i) << " is out of the game." << endl;
        } else {
            cout << playerNames.at(i) << " balance is $" << fixed << showpoint << setprecision(2) << playerCash.at(i) << endl;
            playersWithCash++; // keep track of how many players are still playing because they have cash left
        }
    }
    cout << endl;

    return playersWithCash;
}

/*************************************************************
This function will prompt the user to save the game, if the 
user chooses to, it will save the names and cash balance for 
each player in a file.
**************************************************************/
void SaveGame(const vector<string>& playerNames,
              const vector<double>& playerCash) {

    bool canSave = false;

    for (unsigned int i = 0; i < playerCash.size(); i++) {

        if (!playerCash.at(i) == 0) {
            canSave = true;
        }
    }

    if (canSave == false) {
        cout << "A player must have money to save the game" << endl;
        return;
    }

    if (!ConfirmPrompt("Do you want to save your game")) {
        cout << "Game not saved" << endl;
        return;
    }

    ofstream outFS; // Output file stream handle

    outFS.open(GAME21_FILE);

    if (!outFS.is_open()) {
        throw runtime_error("Could not open file " + GAME21_FILE + " for writing");
    }

    for(unsigned int i = 0; i < playerNames.size(); i++) {
        outFS << playerNames.at(i) << " " << playerCash.at(i) << endl;
    }

    // Done with file, so close it
    outFS.close();

    cout << "Game Saved!" << endl;

    return;
}