#include <AccelStepper.h>
int max_length=310;


void setup() {
  // put your setup code here, to run once:

}

void loop() {
stepper.runToPosition(); 
if (stepper.distanceToGo() == 0){
        stepper.stop();
}
        stepper.moveTo(x);

}


void home_finger(){
  stepper.setMaxSpeed(950);
  stepper.setAcceleration(10000);
   while (!digitalRead(12)) {
      stepper.setSpeed(1000);
      stepper.runSpeed();
      stepper.setCurrentPosition(-len/2);
  }
  
}

void serialEvent() {
  while (Serial.available()) {
    byte inByte= (byte)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
