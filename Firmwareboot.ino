void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  static bool hasRun = false;
  if (!hasRun) {
    Serial.println("Firmware version 1.0");

    unsigned long startTime = millis();
    while (millis() - startTime < 3000) {
      digitalWrite(13, HIGH);
      delay(250);
      digitalWrite(13, LOW);
      delay(250);
    }

    digitalWrite(13, LOW);
    hasRun = true;
  }
}
