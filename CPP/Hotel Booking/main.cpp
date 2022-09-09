/*
Program     : Chapter3PairProgram
Description : This Program will allow users to book a room and
              it will calculate all the costs associated to that booking
Author      : Charles Stanley, Thomas Marxsen
Date Written: 2021.09.28
*/

#include<iostream> // Needed for cin and cout
#include<string>   //Needed for .at function
#include<cstdlib>  //Needed for rand
#include<ctime>    //Needed to seed random with time
using namespace std;

int main(){
    string dow = "?";                   //Inputs
    string roomType = "?";
    int numGuests = 0;

    const int roomSingle = 8;           //Max Number of Rooms
    const int roomDouble = 10;
    const int roomKing = 2;

    int availSingle = 0;                //Rand Results for Rooms
    int availDouble = 0;
    int availKing = 0;

    const int baseRate = 80;            //Base Rate and Special Rates
    const double doubleRate = 0.50;
    const double kingRate = 0.25;
    const double sunMonTue = 0.20;
    const double wedThu = 0.10;

    int costSingle = baseRate;          //Cost Results Before Surcharge
    int costDouble = baseRate;
    int costKing = baseRate;

    int dowCost = 0;                    //Resulting Costs
    int roomCost = 0;
    int surCharge = 0;

    const int twoSur = 10;              //Surchages
    const int threeSur = 18;
    const int fourSur = 32;

    srand(time(0));                     //Seed for Rand

        //HEADER
    cout << endl;
    cout << "Welcome to the Gamer Paradise Hotel" << endl;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << endl << endl;

        //DAY OF WEEK INPUT
    cout << "Which day of the week would you like to check in? ";
    cin >> dow;
    dow.at(0) = toupper(dow.at(0)); //Prepare for Input Test

        //TEST FOR VALID DAY OF WEEK INPUT
    if (!((dow == "Monday") || (dow == "Tuesday") || (dow == "Wednesday") || (dow == "Thursday")
        || (dow == "Friday") || (dow == "Saturday") || (dow == "Sunday"))) {
            cout << "That is an invalid response, please enter a day of the week." << endl;
            return -1;
    }

        //CALCULATION FOR SPECIAL DOW COST
    if ((dow == "Sunday") || (dow == "Monday") || (dow == "Tuesday")) {
        dowCost = baseRate * sunMonTue;
    }
    else if ((dow == "Wednesday") || (dow == "Thursday")) {
        dowCost = baseRate * wedThu;
    }
    else {
        dowCost = 0;
    }

        //CALCULATE AVAILABLE ROOMS WITH RAND
    availSingle = (rand() % roomSingle);
    availDouble = (rand() % roomDouble);
    availKing = (rand() % roomKing);

        //IF STATEMENT FOR NO VACANCY
    if ((availSingle == 0) && (availDouble == 0) && (availKing == 0)) {
        cout << "Sorry, we are all booked for that day." << endl;
        return -2;
    }

        //CALCULATION FOR ROOM COST AFTER SPECIAL RATES
    costSingle += dowCost;
    costDouble = (costDouble * (1 + doubleRate)) + dowCost;
    costKing = (costKing * (1 + kingRate)) + dowCost;

        //DISPLAY OF AVAILABLE ROOMS AND COST
    cout << endl << endl;
    cout << dow << " Available Rooms" << endl;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << availSingle << " single rooms available at $" << costSingle << endl;
    cout << availDouble << " double rooms available at $" << costDouble << endl;
    cout << availKing << " king rooms available at $" << costKing << endl;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl << endl << endl;

        //ROOM SELECTION INPUT
    cout << "What type of room would you like to book? ";
    cin >> roomType;
    roomType.at(0) = tolower(roomType.at(0));
 
        //TEST FOR VALID ROOM INPUT
    if (! ((roomType == "single") || (roomType == "double") || ( roomType == "king"))) {
            cout << "That is an invalid response, please enter a selection from the rooms listed." << endl;
            return -3;
    }

        //TEST FOR ROOM AVAILABILITY
    if ((roomType == "single") && (availSingle > 0)) {
        roomCost = costSingle;
        cout << "Your current booking is $" << roomCost << endl << endl;
    }
    else if ((roomType == "double") && (availDouble > 0)) {
        roomCost = costDouble;
        cout << "Your current booking is $" << roomCost << endl << endl;
    }
    else if ((roomType == "king") && (availKing > 0)) {
        roomCost = costKing;
        cout << "Your current booking is $" << roomCost << endl << endl;
    }
    else {
        cout << "Sorry, there are no rooms available or that type." << endl;
        return -4;
    }

        //INPUT OF NUMBER OF GUESTS
    cout << "How many guests will be staying in the room? ";
    cin >> numGuests;

        //TEST OF MAX
    if (numGuests > 4) {
        cout << "We do not have any rooms for that amount of people, you may need an additional room." << endl;
        return -5;
    }
    if (numGuests < 1) {
        cout << "That is an invalid response, please enter a valid number." << endl;
        return -6;
    }
    
        //SURCHARGE CALCULATION
    switch (numGuests) {
        case 1:
            surCharge = 0;
            break;
        case 2:
            surCharge = twoSur;
            break;
        case 3:
            surCharge = threeSur;
            break;
        case 4:
            surCharge = fourSur;
            break;
        default:
            cout << "We do not have any rooms for that amount of people, you may need an additional room." << endl;
            return -7;
            break;
    }

        //DISPLAY OF SURCHARGE
    if (numGuests == 1){
        cout << "There is no surcharge applied to your booking." << endl;
    }
    if ((roomType == "single") && (numGuests < 3)) {
        cout << "There is a $" << surCharge << " surcharge based on that number of guests." << endl;
    }
    else if ((roomType == "double") && (numGuests <= 4)) {
        cout << "There is a $" << surCharge << " surcharge based on that number of guests." << endl;
    }
    else if ((roomType == "king") && (numGuests < 3)) {
        cout << "There is a $" << surCharge << " surcharge based on that number of guests." << endl;
    }
    else {
        cout << "That exceeds the number of guests we can allow in that room, you may need to book an additional room or upgrade." << endl;
        return -7;
    }
    cout << endl;
    
        //TOTAL COST CALCULATION AND CLOSING
    roomCost += surCharge;
    cout << "That would bring your total booking to: $" << roomCost << endl << endl;
    cout << "Thank you for booking with the Gamer Paradise Hotel, we hope to see you soon!" << endl;

    return 0;
}