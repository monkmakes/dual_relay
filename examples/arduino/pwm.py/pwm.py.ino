const int relayApin = 5;

void setup() {
  Serial.begin(9600);
  Serial.println("brightness (0-255):");
}

void loop() {
  if (Serial.available()) {
    int brightness = Serial.parseInt();
    if (brightness < 0 || brightness > 255) {
      Serial.println("Brightness between 0 and 255");
    }
    else {
      analogWrite(relayApin, brightness);
      Serial.print("Brightness set to: ");
      Serial.println(brightness);
    }
    Serial.println("brightness (0-255):");
  }
}
