#include<Process.h>
int val;
int tempPin = 1;

void setup()
{
// Initialize Bridge
  //Bridge.begin();
  // Initialize Serial
  Serial.begin(9600);
  // Wait until a Serial Monitor is connected.
  //while (!Serial);
  
}
void loop()
{
val = analogRead(tempPin);
float mv = ( val/1024.0)*5000; 
float cel = mv/10;
float farh = (cel*9)/5 + 32;

//Serial.print("TEMPRATURE = ");
Serial.print(cel);
//Serial.print("*C");
Serial.println();
delay(3000);

/*Process p;    // Create a process and call it "p"
  //p.begin("python /home/sk/datasets/regressionRedo.py 24"); // Process that launch the "do_p.py" command
  // Add the parameter to "Wilg"
  //  // Run the process and wait for its termination
  p.begin("python");
p.addParameter("\"/home/sk/datasets/regressionRedo.py 12.0\"");
//p.run();
  p.run();
  // Print arduino logo over the Serial
  // A process output can be read with the stream methods
  while (p.available() > 0) {
    char c = p.read();
    Serial.print(c);

  }

/* uncomment this to get temperature in farenhite 
Serial.print("TEMPRATURE = ");
Serial.print(farh);
Serial.print("*F");
Serial.println();


*/
}
