#define inputCLK 3
#define inputDT 4
int counter =0;
String dir="";
unsigned long last_run = 0;


void setup() {
pinMode(inputCLK,INPUT);
pinMode(inputDT,INPUT);

Serial.begin(9600);
// read the initial state of inputCLK
// Assign to previous state to CLK variable
attachInterrupt(digitalPinToInterrupt(3), shaft_mode, FALLING);

}
void shaft_mode(){
if (millis()- last_run >5 ){
if (digitalRead(inputDT)== 1){
  counter++;
  dir = "CW";
}
else{
  counter --;
  dir = "ccw";
}
last_run = millis();
}
}
void loop() {
Serial.println(dir);
Serial.println(counter);
delay(1000);

}

