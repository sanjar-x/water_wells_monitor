#include <SoftwareSerial.h>
#include <WiFi.h>
#include <HTTPClient.h>

SoftwareSerial serialModem(16, 17);
const char* wifiSSID = "CYBERSWAP";
const char* wifiPassword = "12344321";
const char* apiEndpoint = "https://quduqloyiha.uz/api/message";

void setup() {
  Serial.begin(9600);
  serialModem.begin(9600);
  delay(5000);
  Serial.println("Initialization started...");
  configureSMSModule();
  connectToWiFi();
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected, attempting to reconnect...");
    connectToWiFi();
  }
  checkForIncomingSMS();
}

void configureSMSModule() {
  serialModem.println("AT");
  delay(1000);
  if (serialModem.available()) {
    Serial.println(serialModem.readString());
  }

  serialModem.println("AT+CMGF=1");
  delay(1000);
  if (serialModem.available()) {
    Serial.println(serialModem.readString());
  }

  serialModem.println("AT+CNMI=1,2,0,0,0");
  delay(1000);
  if (serialModem.available()) {
    Serial.println(serialModem.readString());
  }

  Serial.println("SIM800L module connected");
}

void connectToWiFi() {
  Serial.println("Attempting WiFi connection...");
  WiFi.begin(wifiSSID, wifiPassword);

  unsigned long startTime = millis();
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Establishing connection to WiFi...");
    if (millis() - startTime > 30000) {
      Serial.println("Failed to connect to WiFi. Please check your settings");
      return;
    }
  }
  Serial.println("WiFi connection established");
}

void checkForIncomingSMS() {
  if (serialModem.available()) {
    String receivedSMS = serialModem.readString();
    if (receivedSMS.indexOf("+CMT:") != -1) {
      sendHTTPRequest(receivedSMS);
    }
  }
}

void sendHTTPRequest(String messageContent) {
  HTTPClient httpClient;
  httpClient.begin(apiEndpoint);
  httpClient.addHeader("Content-Type", "application/x-www-form-urlencoded");
  String postData = "message_data=" + messageContent;
  int responseCode = httpClient.POST(postData);
  if (responseCode > 0) {
    if (responseCode == 200) {
      Serial.println("Data successfully sent to server");
    } else {
      Serial.print("Failed to send data, server responded with code: ");
      Serial.println(responseCode);
    }
  } else {
    Serial.print("HTTP request failed with error: ");
    Serial.println(httpClient.errorToString(responseCode).c_str());
  }
}
