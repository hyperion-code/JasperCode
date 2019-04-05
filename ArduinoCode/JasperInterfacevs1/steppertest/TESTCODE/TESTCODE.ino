#include <AccelStepper.h>
#include <MultiStepper.h>


AccelStepper stepper(1, 3, 2); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
int len = 310; //length of the rail in steps
int x = 0;
int y = 5;

String input_string = "";

void setup()
{
  Serial.begin(9600);
  // Change these to suit your stepper if you want
  pinMode(12, INPUT);
  pinMode(A3, INPUT);
  pinMode(5, OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(5, LOW);
  stepper.setMaxSpeed(950);
  stepper.setAcceleration(10000);
  while (!digitalRead(A3)) {}
  home_finger();
}

void loop()
{
  actuate_finger(y);
  stepper.moveTo(x);
  if (stepper.distanceToGo() == 0) {
    //stepper.stop();
    digitalWrite(5, HIGH);
  }
  else {
    digitalWrite(5, LOW);
    if (x == 0) {
      home_finger();
    }
    stepper.run();
  }
}

void home_finger() {
  digitalWrite(5, LOW);
  while (!digitalRead(12)) {
    stepper.setSpeed(1000);
    stepper.runSpeed();
    stepper.setCurrentPosition(len );
  }
  digitalWrite(5, HIGH);
}



void serialEvent() {
  while (Serial.available()) {
    int in = Serial.read();
    if (isDigit(in)) input_string += (char)in;
    if (in == 'a') {
      int input_data = input_string.toInt();
      if (input_data >= 0 && input_data < 256){
        x = map(input_data, 0, 255, 0, -len);
      Serial.print("Position: ");
      Serial.println(x);
    }
      else {
        Serial.println("ERROR:Value Exceeds Bounds [0,255]");
      }
      input_string = "";
    }
    else if (in == 'b') {
      y = input_string.toInt();
      Serial.print("Comand: ");
      Serial.println(y);
      input_string = "";
    }
  }
}

void actuate_finger(int input) {
  switch (input) {
    case 0:
      digitalWrite(10, LOW);
      break;
    case 1:
      digitalWrite(10, HIGH);
      break;
    case 2:
      digitalWrite(10, HIGH);
      delay(20);
      digitalWrite(10, LOW);
      y = 0;
      break;
    case 3:
      digitalWrite(10, HIGH);
      delay(10);
      digitalWrite(10, LOW);
      delay(10);
      break;
    case 4:
      digitalWrite(10, HIGH);
      delay(10);
      digitalWrite(10, LOW);
      delay(40);
      break;
    case 5:
     digitalWrite(10, digitalRead(A3));
      break;
  }
}
