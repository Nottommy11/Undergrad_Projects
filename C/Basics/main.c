#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int globalVar = 100;

//FUNCTIONS
int addNumbers(int num1, int num2){
    return num1 + num2;
}

//STRUCTS - Like an object, not associated with a class, like a dictionary
struct Student{
    int age;
    double gpa;
    char grade;
};


int main()
{
//PRINTING
    printf("hello, world\n");
    
//DATA TYPES
    char testGrade = 'A'; //Single 8-bit character
    char name[] = "Thomas"; //array of characters (string)

    //You can make these unsigned
    short age0 = 10;        //At least 16-bits signed integer
    int age1 = 20;          //At least 16-bits signed integer
    long age2 = 30;         //At least 32-bits sigend integer
    long long age3 = 40;    //At least 64-bits signed integer

    float gpa0 = 2.5;       //Single-percision floating point
    double gpa1 = 3.5;      //Double-precision floating point
    long double gpa2 = 3.5; //Extended-precision floating point

    const int IS_TALL = 1;

    //No bool in C, use this
    int isTall;             //0 if false, non-zero if true
    isTall = 1;

    testGrade = 'F';

    printf("%s, your grade is %c \n", name, testGrade);

    /*
    %c character
    %d integer number (base 10)
    %e exponential floating-point number
    %f floating-point number
    %i integer (base 10)
    %o octal number (base 8)
    %s a string of characters
    %u unsigned decimal (integer) number
    %x number in hexadecimal (base 16)
    %% print a percent sign
    \% print a percent sign
    */

//CASTING
   printf("%d \n", (int)3.14);
   printf("%f \n", (double)3/2);

//POINTERS - Basically a memory address
    int num = 10;
    printf("%p \n", &num);  //Print out memory address

    //Pointers variable is int
    int *pNum = &num;       //Store the memory address of num
    printf("%p \n", pNum);  //Memory address of num
    printf("%d \n", *pNum); //Star is d referencing the memory address, will give you the value at that address

//NUMBERS
    printf("%d \n", 2 * 3);     //Basic arithmetic: +, -, /, *
    printf("%d \n", 10 % 3);    //Modulus Operation: Returns remainder of 10/3
    printf("%d \n", 1 + 2 * 3); //Order of operations
    printf("%f \n", 10 / 3.0);  //int's and doubles, floating point and int will always give a float back

    int num1 = 10;
    num1 += 100;                // +=, -=, /=, *=
    printf("%d \n", num1);

    num1++;
    printf("%d \n", num1);

//USER INPUT
    char name1[10];
    printf("Enter your name: ");
    /*
    char (string),
    buffer limit (limits amount of characters user can enter) WANT THIS for protection
    means to input from terminal
    */
    fgets(name1, 10, stdin);
    printf("Hello %s", name1);

    int age4;                       //Can use scanf for an int
    printf("Enter your age: ");
    scanf("%d", &age4);             //Passing pointer
    printf("You are %d \n", age4);

    char grade5;                     //Can use scanf for an char
    printf("Enter your grade: ");
    scanf("%c", &grade5);            //Passing pointer
    printf("Your grade is %c \n", grade5);

    double gpa3;                    //Can use scanf for an double
    printf("Enter your gpa: ");
    scanf("%lf", &gpa3);            //Passing pointer
    printf("Your GPA is %f \n", gpa3);

//ARRAYS
    //int luckNumbers[6] to set size if you don't know values
    int luckyNumbers[] = {4, 8, 15, 16, 23, 42};
    //        indexes     0  1   2   3   4   5
    luckyNumbers[0] = 90;
    printf("%d \n", luckyNumbers[0]);
    printf("%d \n", luckyNumbers[1]);

    //N Dimensional Arrays
    //int numberGrid[2][3]
    int numberGrid[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    numberGrid[0][1] = 99;

    printf("%d \n", numberGrid[0][0]);
    printf("%d \n", numberGrid[0][1]);

//FUNCTIONS - See above main
    //int addNumbers(int num1, int num2); Put This above main if function is below main, like a header file
    int sum = addNumbers(4,60);
    printf("%d \n", sum);

//IF STATEMENTS
    int isStudent = 0;      //Treated as booleans
    int isSmart = 0;

    if(isStudent != 0 && isSmart != 0){
        printf("You are a student\n");
    }
    else if(isStudent != 0 && isSmart == 0){
        printf("You are not a smart student\n");
    }
    else{
        printf("You are not a student and not smart\n");
    }

    // >, <, >=, <=, !=, ==
    if(1 < 3){
        printf("Number comparison was true\n");
    }

    if('a' < 'b'){
        printf("Character comparison was true\n");
    }

//SWITCH STATEMENTS
    char myGrade = 'A';
    switch(myGrade){
        case 'A':
            printf("You Pass\n");
            break;
        case 'F':
            printf("You Fail\n");
            break;
        default:
            printf("Invalid Grade\n");
    }

//WHILE LOOPS
    int index = 1;
    while(index <= 5){
        printf("%d \n", index);
        index++;
    }

    index = 1;

    //do while loop, essentially the same thing, but will execute once before loop starts
    do{
        printf("%d \n", index);
        index++;
        }while(index <= 5);

//FOR LOOPS
    /*
    Declare and instantiate variable,
    Set loop condition or loop guard,
    condition after every loop
    */
    for(int i = 0; i < 5; i++){
        printf("%d \n", i);
    }

//STRUCTS - See above main, similar to objects, about as close as you can get to that
    struct Student student1;
    student1.age = 19;
    student1.gpa = 3.4;
    student1.grade = 'B';

    printf("%d \n", student1.age);

    return 0;
}
