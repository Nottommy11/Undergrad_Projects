#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>

const char *ssid1 = "L&T";
const char *password1 = "schuyler1";

const char *ssid2 = "NASA";
const char *password2 = "oofoofoof";

const char *ssid3 = "CTIS";
const char *password3 = "l0ck3d0ut";

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);
AsyncWebSocket ws("/ws");

double temp = 0, humidity = 0, pressure = 0, altitude = 0, light = 0, speed = 0, volts = 0;
int bearing = 0;
String direction = "";

// int size = 0;
// int iterator = 0;

// int tempArray[12], humidityArray[12], pressureArray[12], altitudeArray[12], lightArray[12], speedArray[12], bearingArray[12], voltsArray[12];
/*
// A linked list node
struct Node
{
	double data;
	struct Node *next;
};

// insert new node at the end of the linked list
void append(struct Node **head, double node_data)
{
	// 1. create and allocate node
	struct Node *newNode = new Node;

	struct Node *last = *head; // used in step 5

	// 2. assign data to the node
	newNode->data = node_data;

	// 3. set next pointer of new node to null as its the last node
	newNode->next = NULL;

	// 4. if list is empty, new node becomes first node
	if (*head == NULL)
	{
		*head = newNode;
		return;
	}

	// 5. Else traverse till the last node
	while (last->next != NULL)
		last = last->next;

	// 6. Change the next of last node
	last->next = newNode;
	return;
}

// display linked list contents
int getSize(struct Node *node)
{
	int count = 0;
	// traverse the list to display each node
	while (node != NULL)
	{
		count++;
		node = node->next;
	}

	return count;
}

// Get ith node data
double getIthNode(struct Node *node, int i)
{
	int count = 0;
	// traverse the list to display each node
	while (node != NULL)
	{
		if (count == i)
		{
			return node->data;
		}
		count++;
		node = node->next;
	}

	return -1;
}

// Remove first node
void removeFirstNode(struct Node **head)
{
	// If linked list is empty, return
	if (*head == NULL)
		return;

	// Store head node
	struct Node *tempVal = *head;

	// Change head node
	*head = (*head)->next;

	// Free memory
	free(tempVal);
} */

/* // Create Linked Lists for each sensor
struct Node *tempList = NULL;
struct Node *humidityList = NULL;
struct Node *pressureList = NULL;
struct Node *altitudeList = NULL;
struct Node *lightList = NULL;
struct Node *speedList = NULL;
struct Node *bearingList = NULL;
struct Node *voltsList = NULL;
 */

const char index_html[] PROGMEM = R"rawliteral(<!DOCTYPE html>
<!DOCTYPE html>
<html>
  <head>
    <title>ESP Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:," />
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.6.0/chart.js"
      integrity="sha512-CWVDkca3f3uAWgDNVzW+W4XJbiC3CH84P2aWZXj+DqI6PNbTzXbl1dIzEHeNJpYSn4B6U8miSZb/hCws7FnUZA=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <style>
      html {
        font-family: Arial, Helvetica, sans-serif;
        text-align: center;
      }
      h2 {
        font-size: 2rem;
        font-weight: bold;
        color: rgb(20, 54, 66);
      }
      span {
        font-size: 1.5rem;
      }
      .top-nav {
        overflow: hidden;
        background-color: rgb(20, 54, 66);
      }
      .nav-text {
        font-size: 1.8rem;
        color: white;
      }
      body {
        margin: 0;
      }
      .content {
        padding: 30px;
        max-width: 600px;
        margin: 0 auto;
      }
      .card {
        background-color: rgb(248, 247, 249);
        box-shadow: 2px 2px 12px 1px rgba(140, 140, 140, 0.5);
        padding-top: 10px;
        padding-bottom: 20px;
        padding-left: 50px;
        padding-right: 50px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
      }
      .data {
        font-size: 1.5rem;
        font-weight: bold;
        color: rgb(20, 54, 66);
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
      }
      #volt-json {
        display: none;
      }
    </style>
    <title>Wind Turbine Data</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:," />
  </head>
  <body>
    <div class="top-nav">
      <h1 class="nav-text">ESP WebSocket Server - Wind Turbine Data</h1>
    </div>
    <div class="content">
      <div class="card">
        <h2>Temp: <span id="temp">%STATE%</span><span> F</span></h2>
        <h2>Humidity: <span id="humidity">%STATE%</span> %</h2>
        <h2>Pressure: <span id="pressure">%STATE%</span> hpa</h2>
        <h2>Altitude: <span id="altitude">%STATE%</span> m</h2>
        <h2>Light: <span id="light">%STATE%</span></h2>
        <h2>Wind Speed: <span id="speed">%STATE%</span> mph</h2>
        <h2>Direction: <span id="direction">%STATE%</span></h2>
        <h2>Voltage: <span id="volts">%STATE%</span> V</h2>
      </div>
    </div>

    <script>
      var gateway = `ws://${window.location.hostname}/ws`;
      var websocket;

      function initWebSocket() {
        console.log("Trying to open a WebSocket connection...");
        websocket = new WebSocket(gateway);
        websocket.onopen = onOpen;
        websocket.onclose = onClose;
        websocket.onmessage = function (event) {
          onData(event);
        };
      }

      function onOpen(event) {
        console.log("Connection opened");
      }

      function onClose(event) {
        console.log("Connection closed");
        setTimeout(initWebSocket, 2000);
      }

      function onData(event) {
        const today = new Date();
        const hour = today.getHours();

        var data = JSON.parse(event.data);
        document.getElementById("temp").innerHTML = data.temp * 1.8 + 32;
        document.getElementById("humidity").innerHTML = data.humidity;
        document.getElementById("pressure").innerHTML = data.pressure;
        document.getElementById("altitude").innerHTML = data.altitude;
        document.getElementById("light").innerHTML = data.light;
        document.getElementById("speed").innerHTML = data.speed;
        document.getElementById("direction").innerHTML = data.direction;
        document.getElementById("volts").innerHTML = data.volts;

        console.log(data);
      }

      window.addEventListener("load", onLoad);
      function onLoad(event) {
        initWebSocket();
      }
    </script>
  </body>
</html>
)rawliteral";

// const char index_html[] PROGMEM = "<!DOCTYPE html><html> <head> <title>ESP Web Server</title> <meta name='viewport' content='width=device-width, initial-scale=1' /> <link rel='icon' href='data:,' /> <script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.6.0/chart.js' integrity='sha512-CWVDkca3f3uAWgDNVzW+W4XJbiC3CH84P2aWZXj+DqI6PNbTzXbl1dIzEHeNJpYSn4B6U8miSZb/hCws7FnUZA==' crossorigin='anonymous' referrerpolicy='no-referrer' ></script> <style> html { font-family: Arial, Helvetica, sans-serif; text-align: center; } h2 { font-size: 2rem; font-weight: bold; color: rgb(20, 54, 66); } span { font-size: 1.5rem; } .top-nav { overflow: hidden; background-color: rgb(20, 54, 66); } .nav-text { font-size: 1.8rem; color: white; } body { margin: 0; } .content { padding: 30px; max-width: 600px; margin: 0 auto; } .card { background-color: rgb(248, 247, 249); box-shadow: 2px 2px 12px 1px rgba(140, 140, 140, 0.5); padding-top: 10px; padding-bottom: 20px; padding-left: 50px; padding-right: 50px; display: flex; flex-direction: column; align-items: flex-start; } .data { font-size: 1.5rem; font-weight: bold; color: rgb(20, 54, 66); display: flex; flex-direction: row; justify-content: space-between; align-items: center; } #volt-json { display: none; } </style> <title>Wind Turbine Data</title> <meta name='viewport' content='width=device-width, initial-scale=1' /> <link rel='icon' href='data:,' /> </head> <body> <div class='top-nav'> <h1 class='nav-text'>ESP WebSocket Server - Wind Turbine Data</h1> </div> <div class='content'> <div class='card'> <h2>Temp: <span id='temp'>%STATE%</span><span> F</span></h2> <h2>Humidity: <span id='humidity'>%STATE%</span> %</h2> <h2>Pressure: <span id='pressure'>%STATE%</span> hpa</h2> <h2>Altitude: <span id='altitude'>%STATE%</span> m</h2> <h2>Light: <span id='light'>%STATE%</span></h2> <h2>Wind Speed: <span id='speed'>%STATE%</span> mph</h2> <h2>Direction: <span id='direction'>%STATE%</span></h2> <h2>Voltage: <span id='volts'>%STATE%</span> V</h2> <button id='update-volts'>Update Chart</button> </div> </div> <script> var gateway = `ws://${window.location.hostname}/ws`; var websocket; function initWebSocket() { console.log('Trying to open a WebSocket connection...'); websocket = new WebSocket(gateway); websocket.onopen = onOpen; websocket.onclose = onClose; websocket.onmessage = function (event) { onData(event); }; } function onOpen(event) { console.log('Connection opened'); } function onClose(event) { console.log('Connection closed'); setTimeout(initWebSocket, 2000); } function onData(event) { const today = new Date(); const hour = today.getHours(); var data = JSON.parse(event.data); document.getElementById('temp').innerHTML = data.temp; document.getElementById('humidity').innerHTML = data.humidity; document.getElementById('pressure').innerHTML = data.pressure; document.getElementById('altitude').innerHTML = data.altitude; document.getElementById('light').innerHTML = data.light; document.getElementById('speed').innerHTML = data.speed; document.getElementById('direction').innerHTML = data.direction; document.getElementById('volts').innerHTML = data.volts; console.log(data); } window.addEventListener('load', onLoad); function onLoad(event) { initWebSocket(); } </script> </body></html>";

void onEvent(AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type,
						 void *arg, uint8_t *data, size_t len)
{
	switch (type)
	{
	case WS_EVT_CONNECT:
		Serial.printf("WebSocket client #%u connected from %s\n", client->id(), client->remoteIP().toString().c_str());
		break;
	case WS_EVT_DISCONNECT:
		Serial.printf("WebSocket client #%u disconnected\n", client->id());
		break;
	case WS_EVT_PONG:
	case WS_EVT_ERROR:
		break;
	}
}

void initWebSocket()
{
	ws.onEvent(onEvent);
	server.addHandler(&ws);
}

bool connectWiFi(const char *ssid, const char *password)
{
	Serial.print("Connecting to WiFi network: ");
	Serial.println(ssid);

	WiFi.begin(ssid, password);
	Serial.setDebugOutput(true);

	WiFi.printDiag(Serial);

	delay(30000);

	if (WiFi.status() == WL_CONNECTED)
	{
		Serial.print("Connected to WiFi network: ");
		Serial.println(ssid);
		return true;
	}

	return false;
}

void setup()
{
	// Serial port for debugging purposes
	Serial.begin(9600);

	// Connect to Wi-Fi
	while (WiFi.status() != WL_CONNECTED)
	{

		if (connectWiFi(ssid1, password1))
			break;
		if (connectWiFi(ssid2, password2))
			break;
		if (connectWiFi(ssid3, password3))
			break;
	}

	// Print ESP Local IP Address
	Serial.println(WiFi.localIP());
	WiFi.printDiag(Serial);

	initWebSocket();

	// Route for root / web page
	server.on("/", HTTP_GET, [](AsyncWebServerRequest *request)
						{ request->send_P(200, "text/html", index_html); });

	// Start server
	server.begin();
}

void setDirection()
{
	switch (bearing)
	{
	case 0:
		direction = "N";
		break;
	case 1:
		direction = "NNE";
		break;
	case 2:
		direction = "NE";
		break;
	case 3:
		direction = "ENE";
		break;
	case 4:
		direction = "E";
		break;
	case 5:
		direction = "ESE";
		break;
	case 6:
		direction = "SE";
		break;
	case 7:
		direction = "SSE";
		break;
	case 8:
		direction = "S";
		break;
	case 9:
		direction = "SSW";
		break;
	case 10:
		direction = "SW";
		break;
	case 11:
		direction = "WSW";
		break;
	case 12:
		direction = "W";
		break;
	case 13:
		direction = "WNW";
		break;
	case 14:
		direction = "NW";
		break;
	case 15:
		direction = "NNW";
		break;
	default:
		direction = "NULL";
	}
}

void receiveSerial()
{
	// Send a JSON-formatted request with key "type" and value "request"
	DynamicJsonDocument inputDoc(1024);

	// Reading the response
	boolean messageReady = false;
	String message = "";

	while (messageReady == false)
	{ // blocking but that's ok
		if (Serial.available())
		{
			message = Serial.readString();
			messageReady = true;
		}
	}

	// Attempt to deserialize the JSON-formatted message
	DeserializationError error = deserializeJson(inputDoc, message);
	if (error)
	{
		Serial.print(F("deserializeJson() failed: "));
		Serial.println(error.c_str());
		return;
	}

	// Extract values
	temp = inputDoc["temp"];
	humidity = inputDoc["humidity"];
	pressure = inputDoc["pressure"];
	altitude = inputDoc["altitude"];
	light = inputDoc["light"];
	speed = inputDoc["speed"];
	bearing = inputDoc["bearing"];
	volts = inputDoc["volts"];

	/* 	append(&tempList, temp);
		append(&humidityList, humidity);
		append(&pressureList, pressure);
		append(&altitudeList, altitude);
		append(&lightList, light);
		append(&speedList, speed);
		append(&bearingList, bearing);
		append(&voltsList, volts); */

	/* 	tempArray[iterator] = temp;
		humidityArray[iterator] = humidity;
		pressureArray[iterator] = pressure;
		altitudeArray[iterator] = altitude;
		lightArray[iterator] = light;
		speedArray[iterator] = speed;
		bearingArray[iterator] = bearing;
		voltsArray[iterator] = volts;
	 */
	// size++;
}

void updateServer()
{
	setDirection();

	String jsonString = "";
	StaticJsonDocument<200> outputDoc;
	JsonObject obj = outputDoc.to<JsonObject>();

	// int size = getSize(tempList);

	/* if (size > 12)
	{
		removeFirstNode(&tempList);
		removeFirstNode(&humidityList);
		removeFirstNode(&pressureList);
		removeFirstNode(&altitudeList);
		removeFirstNode(&lightList);
		removeFirstNode(&speedList);
		removeFirstNode(&bearingList);
		removeFirstNode(&voltsList);
		size = size - 1;
	} */

	// int tempArr[size], humidityArr[size], pressureArr[size], altitudeArr[size], lightArr[size], speedArr[size], bearingArr[size], voltsArr[size];

	/* 	for (int i = 0; i < size; i++)
		{
			String tempStr = "temp" + String(i);
			String humidityStr = "humidity" + String(i);
			String pressureStr = "pressure" + String(i);
			String altitudeStr = "altitude" + String(i);
			String lightStr = "light" + String(i);
			String speedStr = "speed" + String(i);
			String bearingStr = "bearing" + String(i);
			String voltsStr = "volts" + String(i);

			Serial.println(tempStr);
			Serial.println(getIthNode(tempList, i));

			obj[tempStr] = getIthNode(tempList, i);
			obj[humidityStr] = getIthNode(humidityList, i);
			obj[pressureStr] = getIthNode(pressureList, i);
			obj[altitudeStr] = getIthNode(altitudeList, i);
			obj[lightStr] = getIthNode(lightList, i);
			obj[speedStr] = getIthNode(speedList, i);
			obj[bearingStr] = getIthNode(bearingList, i);
			obj[voltsStr] = getIthNode(voltsList, i);
		} */

	/* obj["temp"] = copyArray(tempArr, outputDoc.to<JsonArray>());
	obj["humidity"] = copyArray(humidityArr, outputDoc.to<JsonArray>());
	obj["pressure"] = copyArray(pressureArr, outputDoc.to<JsonArray>());
	obj["altitude"] = copyArray(altitudeArr, outputDoc.to<JsonArray>());
	obj["light"] = copyArray(lightArr, outputDoc.to<JsonArray>());
	obj["speed"] = copyArray(speedArr, outputDoc.to<JsonArray>());
	obj["bearing"] = copyArray(bearingArr, outputDoc.to<JsonArray>());
	obj["volts"] = copyArray(voltsArr, outputDoc.to<JsonArray>()); */
	/*
		for (int i = 0; i < 12; i++)
		{
			String tempStr = "temp" + String(i);
			String humidityStr = "humidity" + String(i);
			String pressureStr = "pressure" + String(i);
			String altitudeStr = "altitude" + String(i);
			String lightStr = "light" + String(i);
			String speedStr = "speed" + String(i);
			String bearingStr = "bearing" + String(i);
			String voltsStr = "volts" + String(i);

			obj[tempStr] = tempArray[i];
			obj[humidityStr] = humidityArray[i];
			obj[pressureStr] = pressureArray[i];
			obj[altitudeStr] = altitudeArray[i];
			obj[lightStr] = lightArray[i];
			obj[speedStr] = speedArray[i];
			obj[bearingStr] = bearingArray[i];
			obj[voltsStr] = voltsArray[i];
		}

		if (iterator == 11)
		{
			iterator = 0;
		}
		else
		{
			iterator++;
		} */

	obj["temp"] = temp;
	obj["humidity"] = humidity;
	obj["pressure"] = pressure;
	obj["altitude"] = altitude;
	obj["light"] = light;
	obj["speed"] = speed;
	obj["direction"] = direction;
	obj["volts"] = volts;

	serializeJson(outputDoc, jsonString);
	ws.textAll(jsonString);
	Serial.println(jsonString);
}

void loop()
{
	ws.cleanupClients();

	receiveSerial();

	updateServer();
}
