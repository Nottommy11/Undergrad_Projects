#include <iostream>
#include <map>
using namespace std;

int main() {
    // Create a map
    map<char, int> myMap = {
            {'T', 1},
            {'C', 2},
            {'G', 3},
            {'A', 4}
    };
    cout << myMap['T'] << endl;

    // Insert a new element
    myMap['u'] = 5;
    cout << myMap['u'] << endl;

    // Insert a new element using insert()
    myMap.insert(pair<char, int>('j', 6));
    cout << myMap['j'] << endl;

    // Insert a new element using insert() and a pair
    pair<char, int> p1('k', 7);
    myMap.insert(p1);
    cout << myMap['k'] << endl;
    cout << p1.first << ", " << p1.second << endl;

    // Erase an element
    myMap.erase('k');
    myMap.erase(p1.first);
    cout << myMap['k'] << endl;
    cout << p1.first << ", " << p1.second << endl;

    // Clear the map
    //myMap.clear();

    // Check if the map is empty
    if (myMap.empty()) {
        cout << "The map is empty" << endl;
    }
    else {
        cout << "The map is not empty" << endl;
    }

    // Check the size of the map
    cout << "The size of the map is " << myMap.size() << endl;

    // Iterate through the map
    cout << "Using auto" << endl;
    for(auto & itr : myMap) {
        cout << itr.first << ": " << itr.second << endl;
    }
    //OR
    cout << "Using pointer and dereference" << endl;
    for(auto itr = myMap.begin(); itr != myMap.end(); itr++) {
        cout << (*itr).first << ": " << (*itr).second << endl;
    }
    //OR
    cout << "Using pointer and arrow" << endl;
    for(auto itr = myMap.begin(); itr != myMap.end(); itr++) {
        cout << itr->first << ": " << itr->second << endl;
    }

    //EXAMPLE USE CASE
    string test = "Hello world my name is Thomas!";
    map<char, int> charCount;

    for(int i = 0; i < test.length(); i++) {
        char letter = test[i];

        // Check if the letter is in the map
        if(charCount.find(letter) == charCount.end()) {
            charCount[letter] = 1;
        }
        else {
            charCount[letter]++;
        }
        cout << letter << ": " << charCount[letter] << endl;
    }

    for(auto & itr : charCount) {
        cout << itr.first << ": " << itr.second << endl;
    }
}
