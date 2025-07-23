bool hasRun = false;  // Flag to track if firmware message and blink ran

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (!hasRun) {
    // Print firmware version
    Serial.println("Firmware version 1.0");

    // Blink LED for 3 seconds
    unsigned long startTime = millis();
    while (millis() - startTime < 3000) {
      digitalWrite(13, HIGH);
      delay(250);
      digitalWrite(13, LOW);
      delay(250);
    }

    // Make sure LED is off
    digitalWrite(13, LOW);

    // Mark as completed so it doesn't repeat
    hasRun = true;
  }

  // Add other code here (if any)
}
