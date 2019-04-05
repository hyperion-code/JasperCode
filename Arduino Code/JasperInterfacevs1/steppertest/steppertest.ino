// Bounce.pde
// -*- mode: C++ -*-
//
// Make a single stepper bounce from one limit to another
//
// Copyright (C) 2012 Mike McCauley
// $Id: Random.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $


// Define a stepper and the pins it will use
AccelStepper stepper(1,3,2); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
int len=310;
void setup()
{  
  // Change these to suit your stepper if you want
    pinMode(12, INPUT);
        pinMode(A3, INPUT);

    Serial.begin(9600);

  stepper.moveTo(len/2);
  
}

void loop()
{
  if(digitalRead(A3)){
    // If at the end of travel go to the other end
    if (stepper.distanceToGo() == 0){
        stepper.stop();
  stepper.runToPosition(); 

      int x=random(-len/2,len/2);
            stepper.moveTo(x);
  Serial.println(x);

    }
    
    stepper.run();
  }
}
