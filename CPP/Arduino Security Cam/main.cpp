#include <Arduino.h>
#include <Stepper.h>
#include <AccelStepper.h>
#include <Servo.h>

// Create servo object to control a servo
Servo yServo;

// Set pins for stepper
AccelStepper myStepper(4, 8, 10, 9, 11);

// Set pins for joystick
int xPin = A0;
int yPin = A1;

// Set pins for servo
int servoPin = 7;

// Declare variables for reading joystick
int WVx = 0;
int WVy = 0;
int xVal = 0;
int yVal = 0;

void readAnalog();

void setup()
{

  Serial.begin(9600);

  myStepper.setMaxSpeed(650);
  myStepper.setAcceleration(200);
  myStepper.setCurrentPosition(600);

  myStepper.setSpeed(400);

  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  pinMode(servoPin, OUTPUT);

  yServo.attach(servoPin); // attaches the servo on pin 9 to the servo object
  yServo.write(20);        // set servo to mid-point
}

void loop()
{

  readAnalog();

  // Move stepper left
  if (WVx > 300)
  {
    myStepper.setPinsInverted(false);
    myStepper.setSpeed(WVx);
    myStepper.runSpeed();
    }
  // Move stepper right
  else if (WVx < 296)
  {
    myStepper.setPinsInverted(true);
    myStepper.setSpeed(abs(WVx - 600));
    myStepper.runSpeed();
  }

  // Move servo
  yServo.write(WVy + 20);
}

void readAnalog()
{
  // Read joystick values
  xVal = analogRead(xPin);
  // Convert to 0-600 range
  WVx = (600. / 1023.) * xVal;

  yVal = analogRead(yPin);
  // Convert to 0-80 range
  WVy = (60. / 1023.) * yVal;

  // Print joystick values
  Serial.print("X: ");
  Serial.print(WVx);
  Serial.print(" Y: ");
  Serial.println(WVy);
}
