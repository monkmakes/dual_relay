const int relayApin = 5;
const int relayBpin = 3;

void setup() {
  pinMode(relayApin, OUTPUT);
  pinMode(relayBpin, OUTPUT);
}

void loop() {
  digitalWrite(relayApin, HIGH);
  digitalWrite(relayBpin, LOW);
  delay(500);
  digitalWrite(relayApin, LOW);
  digitalWrite(relayBpin, HIGH);
  delay(500);
}
