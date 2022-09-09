/*************************************************************
Header file with all the Game 21 function prototypes
Programmer: Thomas Marxsen
Date Written: 2021.12.12
**************************************************************/
#ifndef GAME21_H_INCLUDED
#define GAME21_H_INCLUDED

#include <string>
#include <vector>

using namespace std;

bool ConfirmPrompt(const string prompt);

void DisplayGameIntro();

void LoadGame(vector<string>& playerNames,
              vector<double>& playerCash);

void DisplayPreviousGame(vector<string>& playerNames,
                         vector<double>& playerCash);

void GetPlayerNames(vector<string>& playerNames);

int DealPlayers(const vector<string>& playerNames,
                vector<double>& playerBets,
                const vector<double>& playerCash,
                vector<int>& playerCardsTotal);

int DealDealer(const int highestHand);

void DisplayWinningPlayers(const vector<string>&playerNames,
                           const vector<double>& playerBets,
                           vector<double>& playerCash,
                           const vector<int>& playerCardsTotal,
                           const int dealerCardsTotal);

int RoundSummary(const vector<string>& playerNames,
                 const vector<double>& playerCash);

void SaveGame(const vector<string>& playerNames,
              const vector<double>& playerCash);

#endif // GAME21_H_INCLUDED

