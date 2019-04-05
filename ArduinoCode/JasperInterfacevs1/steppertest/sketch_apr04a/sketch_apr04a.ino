#include <AccelStepper.h>
#include <MultiStepper.h>


AccelStepper stepper(1, 3, 2); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
int len = 310;
int x = 0;
void setup()
{
  // Change these to suit your stepper if you want
  pinMode(12, INPUT);
  pinMode(A3, INPUT);
  pinMode(5, OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(5, LOW);
  stepper.setMaxSpeed(950);
  stepper.setAcceleration(10000);
  while (!digitalRead(A3)) {}
  while (!digitalRead(12)) {
    stepper.setSpeed(1000);
    stepper.runSpeed();
    stepper.setCurrentPosition(len / 2);
  }


}

void loop()
{
  digitalWrite(10, digitalRead(A3));

  if (digitalRead(A3)) {
    stepper.moveTo(x);
    stepper.run();
    if (stepper.distanceToGo() == 0) {
      stepper.stop();
    }
  }
  else {
    digitalWrite(5, HIGH));
  }
}
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    int input_data = (int)Serial.read();
    x = map(input_data, 0, 255, 0, max_ength)
  }
