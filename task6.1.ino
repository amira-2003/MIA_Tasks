//include wire library for i2c communication protocol
#include <Wire.h>
//declare global variables 
float RateYaw;
float AccX , AccY, AccZ;
float AngleYaw;
uint32_t LoopTimer;

float RateCalibrationYaw;
float RateCalibrationNumber;
float kalmanAngleYaw=0;
float kalmanUNCERTAIN_YAW =0;
float KalmanOUTPUT[] ={0,0};
// first index is the angle prediction and second index is uncertainty of the prediction


void KalmanFilter(float K_State  , float K_Uncertainty  , float K_Input ,float K_measurement ){
  // K_Input is rotation rate 
  // K_measurement is accelerometer angle
  // K_State  is angle calculated with the kalman filter
K_State = K_State + 0.004* K_Input;
K_Uncertainty = K_Uncertainty + 0.004*0.004*4*4;
float K_Gain = K_Uncertainty *1/(1*K_Uncertainty+3*3);
K_State = K_State + K_Gain*(K_measurement -  K_State );
K_Uncertainty  = (1-K_Gain)*K_Uncertainty;

KalmanOUTPUT[0]= K_State ;
KalmanOUTPUT[1]= K_Uncertainty ;
}



//declare function called gyro signals to start reading rotation rates, acceleration and angles from MPU6050 
void gyro_signals(void){

// (0x68) is the address of MPU6050 , (0x1A) is DLPF (low pass filter) , (0x05) is cf(cutof frequency) its value 10Hz
Wire.beginTransmission(0x68);
Wire.write(0x1A);
Wire.write(0x05);
Wire.endTransmission();

// (0x1C) represents the sensitivity scale factor, (0x10) represents 
Wire.beginTransmission(0x68);
Wire.write(0x1C);
Wire.write(0x10);
Wire.endTransmission();

// 3B is ACCEL_XOUT_H
Wire.beginTransmission(0x68);
Wire.write(0x3B);
Wire.endTransmission();

// accessing (0x68.6) to pull information of the six registors 43-48
Wire.requestFrom(0x68, 6);
// read accelerometer measurements around x,y,z axis
int16_t AccXLSB = Wire.read() << 8 | Wire.read();
int16_t AccYLSB = Wire.read() << 8 | Wire.read();
int16_t AccZLSB = Wire.read() << 8 | Wire.read();
Wire.beginTransmission(0x68);
Wire.write(0x1B);
Wire.write(0x8);
Wire.endTransmission();

// (0x43) is gyro x_out high
Wire.beginTransmission(0x68);
Wire.write(0x43);
Wire.endTransmission();
// read gyro measurements around x,y,z axis
Wire.requestFrom(0x68, 6);
int16_t GyroX = Wire.read() << 8 | Wire.read();
int16_t GyroY = Wire.read() << 8 | Wire.read();
int16_t GyroZ = Wire.read() << 8 | Wire.read();

RateYaw = (float)GyroZ/65.5;
// rate of yaw angle to convert units to /s
AccX = (float)AccXLSB / 4096 -0.05;
AccY = (float)AccYLSB / 4096 +0.01;
AccZ = (float)AccZLSB / 4096-0.11;

//calculating yaw angle 
AngleYaw = atan(AccZ/sqrt(AccX*AccX + AccY*AccY))* 1/(3.14/180);

}




void setup() {
  Serial.begin(57600);
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH);
  Wire.setClock(400000);
  Wire.begin();
  delay(250);
  Wire.beginTransmission(0x68);
  Wire.write(0x6B);
  Wire.write(0x00);
  Wire.endTransmission();
  for (RateCalibrationNumber = 0  ; RateCalibrationNumber<2000   ; RateCalibrationNumber++){
  gyro_signals();
  RateCalibrationYaw+= RateYaw;
  delay(10);
  }
  RateCalibrationYaw /= 2000;
  LoopTimer = micros();
}

void loop() {
gyro_signals();
RateYaw -= RateCalibrationYaw;
KalmanFilter(kalmanAngleYaw,kalmanUNCERTAIN_YAW, RateYaw,AngleYaw);
kalmanAngleYaw = KalmanOUTPUT[0];
kalmanUNCERTAIN_YAW = KalmanOUTPUT[1];

Serial.print("YawAngle[] =   ");
Serial.print(kalmanAngleYaw);
while(micros() - LoopTimer <4000);
LoopTimer = micros();

}
