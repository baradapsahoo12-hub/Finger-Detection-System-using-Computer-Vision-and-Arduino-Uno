int ledPins[5] = {8, 9, 10, 11, 12}; // Thumb, Index, Middle, Ring, Pinky

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
}

void loop() {
  if (Serial.available() >= 5) {  
    for (int i = 0; i < 5; i++) {
      int state = Serial.read();  // Read each finger state (0 or 1)

      if (state == '1') {
        digitalWrite(ledPins[i], HIGH);
      } else {
        digitalWrite(ledPins[i], LOW);
      }
    }
  }
}