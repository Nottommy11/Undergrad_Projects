/*************************************************************
TODO:
Description: Header file to initialize functions
Pair Programmer #1 Name: Thomas Marxsen
Pair Programmer #1 Replit: https://replit.com/join/dbqvrgoloa-nottommy11
Pair Programmer #2 Name: Jadyn Keller
Pair Programmer #2 Replit: https://replit.com/join/umoxnknugd-jakell10
Date Written: 11/17/2021
**************************************************************/
#ifndef HIGH_LOW_H_INCLUDED		// if the constant variable is NOT defined
#define HIGH_LOW_H_INCLUDED		// then define it and include the following code

#include <vector>
using namespace std;

void DisplayHeading();
int GetNumber();
void DisplayHighLowMsg(int previousDiff, int currentDiff);
void DisplayTemp(int currentDiff);
bool PlayAgain();
void DisplayResults(const vector<int>& rounds);

#endif // HIGH_LOW_H_INCLUDED
