#include<iostream>
#include<string>
using namespace std;

void EncryptMessage();
void DecryptMessage();

string MessageInput();
int MessageKey();

int main(){
    bool continueLoop = 1;
    char input;
    string answer;

    cout << endl;
    cout << "=======================================================" << endl;
    cout << "WELCOME TO THE MASTER TEXT DECIPHERER" << endl;
    cout << "=======================================================" << endl << endl;

    while(continueLoop){
        cout << "Would you like to decrypt or encrypt a message?\n";
        cout << "(Enter encrypt or decrypt): ";
        cin >> answer;
        cout << endl;
        cout << "=======================================================" << endl;
        cout << "=======================================================" << endl << endl;

        if(answer == "decrypt"){
            DecryptMessage();
        }
        else if(answer == "encrypt"){
            EncryptMessage();
        }
        else{
            cout << "Invalid Response" << endl << endl;
        }

        cout << "=======================================================" << endl;
        cout << "=======================================================" << endl << endl;
        cout << "Would you like to decipher another message? (y/n): ";
        cin >> input;
        cout << endl;
        cout << "=======================================================" << endl;
        cout << "=======================================================" << endl << endl;

        if(input != 'y'){
            continueLoop = 0;
        }
    }

    cout << "Thank you for using the Master Text Decipherer! Goodbye" << endl << endl;
    return 0;
}

void EncryptMessage(){
    string input;
    int key;
    string encryptedText;
    char temp;

    input = MessageInput();
    key = MessageKey();

    encryptedText.resize(input.length());

    for(int i = 0; i < input.length(); i++){
        temp = input[i];
        temp += key;
        encryptedText[i] = (char) temp;
    }

    cout << "Encrypted message: " << endl << encryptedText << endl << endl;
    return;
}

void DecryptMessage(){
    string input;
    int key;
    string decryptedText;
    char temp;

    input = MessageInput();
    key = MessageKey();

    decryptedText.resize(input.length());

    for(int i = 0; i < input.length(); i++){
        temp = input[i];
        temp -= key;
        decryptedText[i] = (char) temp;
    }

    cout << "Decrypted message: " << endl << decryptedText << endl << endl;
    return;
}

string MessageInput(){
    string message;

    cout << "Enter message here: \n";
    cin.ignore();
    getline(cin, message);
    cout << endl;

    return message;
}

int MessageKey(){
    int key;

    cout << "Enter the key here (positive integer): ";
    cin >> key;
    cout << endl;
    cout << "=======================================================" << endl << endl;
    
    return key;
}