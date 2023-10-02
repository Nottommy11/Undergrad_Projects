#include <Arduino.h>

#include <SD.h>
#include <SPI.h>
#include <DS3231.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <QMC5883LCompass.h>
#include <ArduinoJson.h>

const int photoResistor = A0; // Photoresistor at Arduino analog pin A0

DS3231 clock;
RTCDateTime dt;

File myFile;

int pinCS = 53; // Pin 10 on Arduino Uno

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
                     // Adafruit_BME280 bme(BME_CS); // hardware SPI
                     // Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI
unsigned status;

const int voltageSensorPin = A1; // sensor pin
float vIn;                       // measured voltage (3.3V = max. 16.5V, 5V = max 25V)
float vOut;
float voltageSensorVal;     // value on pin A3 (0 - 1023)
const float factor = 5.128; // reduction factor of the Voltage Sensor shield
const float vCC = 5.00;     // Arduino input voltage (measurable by voltmeter)

// Mode Control (MODE)
const byte qmc5883l_mode_stby = 0x00;
const byte qmc5883l_mode_cont = 0x01;
// Output Data Rate (ODR)
const byte qmc5883l_odr_10hz = 0x00;
const byte qmc5883l_odr_50hz = 0x04;
const byte qmc5883l_odr_100hz = 0x08;
const byte qmc5883l_odr_200hz = 0x0C;
// Full Scale Range (RNG)
const byte qmc5883l_rng_2g = 0x00;
const byte qmc5883l_rng_8g = 0x10;
// Over Sample Ratio (OSR)
const byte qmc5883l_osr_512 = 0x00;
const byte qmc5883l_osr_256 = 0x40;
const byte qmc5883l_osr_128 = 0x80;
const byte qmc5883l_osr_64 = 0xC0;

int x_value;
int y_value;
int z_value;
int azimuth;  // 0° - 359°
byte bearing; // 0 - 15 (N, NNE, NE, ENE, E, ...)
char direction[strlen("NNE") + 1];
char buffer[strlen("X=-99999 | Y=-99999 | Z=-99999 | A=259° | B=15 | D=NNE") + 1];

String myDirection = "";

QMC5883LCompass compass;

int windPin = A3;
float voltageMax = 2.0;
float voltageMin = 0.4;
float voltageConversionConstant = .004882814;
float sensorVoltage = 0.0;

float windSpeedMin = 0.0;
float windSpeedMax = 32.0;

int windSpeed = 0;
int prevWindSpeed = 0;

float speedMPH = 0.0;

String fileName = "test.txt";

void testSD()
{

  while (dt.year == 0)
  {
    Serial.println("Waiting for RTC");

    dt = clock.getDateTime();
  }

  fileName = "";
  fileName.concat(dt.year);
  // fileName.concat("-");
  fileName.concat(dt.month);
  // fileName.concat("-");
  fileName.concat(dt.day);
  fileName.concat(".txt");

  // SD Card Initialization
  if (SD.begin())
  {
    Serial.println("SD card is ready to use.");
  }
  else
  {
    Serial.println("SD card initialization failed");
    return;
  }

  /*  Serial.print("File: ");
   Serial.println(fileName);
   Serial.println(SD.exists(fileName) ? "File exists" : "File doesn't exist"); */

  /*   if (SD.exists(fileName))
    {
      SD.remove(fileName);
    } */

  // Reading the file
  myFile = SD.open(fileName);

  Serial.print("File: ");
  Serial.println(fileName);

  if (myFile)
  {
    Serial.println("Read:");
    // Reading the whole file
    while (myFile.available())
    {
      Serial.write(myFile.read());
    }
    myFile.close();
  }
  else
  {
    Serial.print("error opening ");
    Serial.println(fileName);

    while (!myFile)
    {
      Serial.println("Trying to open, this file is probably empty");
      myFile = SD.open(fileName, FILE_WRITE);
    }

    if (myFile)
    {
      Serial.println("File opened");

      myFile.println("Time, Temp, Humidity, Pressure, Altitude, Light,  Wind Speed, Wind Direction, Voltage In");
      myFile.close();
    }
  }
}

void testBME()
{
  // Test if the BME280 is connected
  Serial.println(F("BME280 test"));

  // default settings
  status = bme.begin(0x76);
  // You can also pass in a Wire library object like &Wire2
  // status = bme.begin(0x76, &Wire2)
  if (!status)
  {
    Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
    Serial.print("SensorID was: 0x");
    Serial.println(bme.sensorID(), 16);
    Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
    Serial.print("        ID of 0x56-0x58 represents a BMP 280,\n");
    Serial.print("        ID of 0x60 represents a BME 280.\n");
    Serial.print("        ID of 0x61 represents a BME 680.\n");
    while (1)
      delay(10);
  }

  Serial.println("-- Default Test --");

  Serial.println();
}

void setup()
{
  Serial.begin(9600);

  pinMode(photoResistor, INPUT); // Set pResistor - A0 pin as an input (optional)

  // Initialize DS3231
  Serial.println("Initialize DS3231");
  ;
  clock.begin();

  pinMode(pinCS, OUTPUT);

  testSD();

  testBME();

  compass.init();
  compass.setCalibration(-821, 380, -177, 771, -1655, -1363);
}

void writeToFile()
{

  switch (bearing)
  {
  case 0:
    myDirection = "N";
    break;
  case 1:
    myDirection = "NNE";
    break;
  case 2:
    myDirection = "NE";
    break;
  case 3:
    myDirection = "ENE";
    break;
  case 4:
    myDirection = "E";
    break;
  case 5:
    myDirection = "ESE";
    break;
  case 6:
    myDirection = "SE";
    break;
  case 7:
    myDirection = "SSE";
    break;
  case 8:
    myDirection = "S";
    break;
  case 9:
    myDirection = "SSW";
    break;
  case 10:
    myDirection = "SW";
    break;
  case 11:
    myDirection = "WSW";
    break;
  case 12:
    myDirection = "W";
    break;
  case 13:
    myDirection = "WNW";
    break;
  case 14:
    myDirection = "NW";
    break;
  case 15:
    myDirection = "NNW";
    break;
  default:
    myDirection = "NULL";
  }

  // Serial.println("Writing to file...");

  myFile.print(dt.hour);
  myFile.print(":");
  myFile.print(dt.minute);
  myFile.print(":");
  myFile.print(dt.second);

  myFile.print(", ");
  myFile.print(bme.readTemperature());
  myFile.print(", ");
  myFile.print(bme.readHumidity());
  myFile.print(", ");
  myFile.print(bme.readPressure() / 100.0F);
  myFile.print(", ");
  myFile.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
  myFile.print(", ");
  myFile.print(analogRead(photoResistor));
  myFile.print(", ");
  myFile.print(speedMPH);
  myFile.print(", ");
  myFile.print(myDirection);
  myFile.print(", ");
  myFile.print(vIn);
  myFile.println("");
  myFile.close(); // close the file
}

void readVolts()
{
  voltageSensorVal = analogRead(voltageSensorPin); // read the current sensor value (0 - 1023)
  vOut = (voltageSensorVal / 1024) * vCC;          // convert the value to the real voltage on the analog pin
  vIn = vOut * factor;                             // convert the voltage on the source by multiplying with the factor

  /*   Serial.print("Voltage = ");
    Serial.print(vIn);
    Serial.println("V"); */
}

void readCompass()
{
  compass.read(); // Read compass values via I2C

  x_value = compass.getX();
  y_value = compass.getY();
  z_value = compass.getZ();
  azimuth = compass.getAzimuth(); // Calculated from X and Y value
  bearing = compass.getBearing(azimuth);

  compass.getDirection(direction, azimuth);
  direction[3] = '\0';

  /*  sprintf(buffer,
           "X=%6d | Y=%6d | Z=%6d | A=%3d° | B=%02hu | %s",
           x_value,
           y_value,
           z_value,
           azimuth,
           bearing,
           direction);
   Serial.println(buffer); */

  delay(200);
}

void readAnemometer()
{
  int sensorValue = analogRead(windPin);

  float voltage = sensorValue * (5.0 / 1023.0);

  sensorVoltage = sensorValue * voltageConversionConstant;

  if (sensorVoltage <= voltageMin)
  {
    windSpeed = 0;
  }
  else
  {
    windSpeed = ((sensorVoltage - voltageMin) * windSpeedMax / (voltageMax - voltageMin)) * 2.232694;
  }

  speedMPH = ((windSpeed * 3600) / 1609.344);

  /* if (windSpeed != prevWindSpeed)
  {
    Serial.print("Wind Speed: ");
    Serial.print(windSpeed);
    Serial.print(" m/s");
    Serial.print(" | ");
    Serial.print("Voltage: ");
    Serial.print(sensorVoltage);
    Serial.print(" V");
    Serial.print(" | ");
    Serial.print("Sensor Value: ");
    Serial.print(sensorValue);
    Serial.print(" | ");
    Serial.print("Wind Speed: ");
    Serial.println(speedMPH);
  } */
}

void sendDataESP()
{
  String jsonString = "";
  StaticJsonDocument<200> doc;
  JsonObject obj = doc.to<JsonObject>();

  obj["temp"] = bme.readTemperature();
  obj["humidity"] = bme.readHumidity();
  obj["pressure"] = bme.readPressure() / 100.0F;
  obj["altitude"] = bme.readAltitude(SEALEVELPRESSURE_HPA);
  obj["light"] = analogRead(photoResistor);
  obj["speed"] = speedMPH;
  obj["bearing"] = bearing;
  obj["volts"] = vIn;
  serializeJson(doc, jsonString);
  Serial.println(jsonString);
}

void loop()
{
  dt = clock.getDateTime();

  readVolts();

  readCompass();

  readAnemometer();

  sendDataESP();

  // Create/Open file
  myFile = SD.open(fileName, FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile)
  {
    writeToFile();

    // Serial.println("Done.");
  }
  else
  {
    Serial.print("error opening ");
    Serial.println(fileName);
  }

  // Delay in seconds
  delay(30 * 1000);

  // Delay in minutes
  // delay(30 * 60 * 1000);

  // Delay in hours
  // delay(1 * 60 * 60 * 1000);
}
