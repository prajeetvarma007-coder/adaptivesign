// AdaptiveSign - Flex Sensor Calibration
// Records minimum and maximum values for each finger

const int FLEX1 = 34;  // Thumb
const int FLEX2 = 35;  // Index
const int FLEX3 = 32;  // Middle
const int FLEX4 = 33;  // Ring
const int FLEX5 = 25;  // Little

int flexMin[5] = {4095, 4095, 4095, 4095, 4095};
int flexMax[5] = {0, 0, 0, 0, 0};

void setup() {
  Serial.begin(115200);

  delay(1000);

  Serial.println();
  Serial.println("================================");
  Serial.println(" AdaptiveSign Flex Calibration");
  Serial.println("================================");
  Serial.println();

  Serial.println("Keep all fingers STRAIGHT.");
  Serial.println("Collecting minimum values...");
  delay(3000);

  for (int i = 0; i < 100; i++) {
    updateCalibration();
    delay(20);
  }

  Serial.println("Straight position recorded.");
  Serial.println();

  Serial.println("Now CLOSE all fingers.");
  Serial.println("Collecting maximum values...");
  delay(3000);

  for (int i = 0; i < 100; i++) {
    updateCalibration();
    delay(20);
  }

  Serial.println("Closed position recorded.");
  Serial.println();

  printCalibration();
}

void loop() {
  // Calibration runs only once.
}

void updateCalibration() {

  int values[5];

  values[0] = analogRead(FLEX1);
  values[1] = analogRead(FLEX2);
  values[2] = analogRead(FLEX3);
  values[3] = analogRead(FLEX4);
  values[4] = analogRead(FLEX5);

  for (int i = 0; i < 5; i++) {

    if (values[i] < flexMin[i]) {
      flexMin[i] = values[i];
    }

    if (values[i] > flexMax[i]) {
      flexMax[i] = values[i];
    }
  }
}

void printCalibration() {

  Serial.println("================================");
  Serial.println(" Calibration Results");
  Serial.println("================================");

  const char* fingers[5] = {
    "Thumb",
    "Index",
    "Middle",
    "Ring",
    "Little"
  };

  for (int i = 0; i < 5; i++) {

    Serial.print(fingers[i]);
    Serial.print(" : MIN = ");
    Serial.print(flexMin[i]);

    Serial.print(" | MAX = ");
    Serial.println(flexMax[i]);
  }

  Serial.println();
  Serial.println("Copy these values for the next stage.");
}
