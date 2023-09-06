# MIA_tasks
MIA_tasks includes electrical  tasks of different branches hardware and software.
## task6.1:
[wokwi link:simulation ](https://wokwi.com/projects/375150491946124289)

Q: If the Sensor is surrounded by a noisy environment, what type of filter could used ?

ANSWER: noise and errors
In the ideal word, sensors data with applied formulas would provide us precise and exact angles. The reality is different as some factors affect the sensors output.

Typically, when you move around with an accelerometer it experiences movement accelerations. Additional acceleration values may affect the orientation accuracy. Another accelerometer related problem is the noise: unwanted disturbance in an electrical signal. The accelerometer is able to measure any angle, however its readings are noisy and have a certain margin of error even with a low pass filter.
On the other hand, gyroscopes are subject to bias instabilities, in which the initial zero reading of the gyroscope will cause drift over time due to integration of inherent imperfections and noise within the device.
So, what can we do? There are different algorithms to solve this problems. The one we are going to use is known as complementary filter. Idea behind complementary filter is to take slow moving signals from accelerometer and fast moving signals from a gyroscope and combine them. It is ideal to implement with Arduino: easy to use, low cost of processing and good precision.

### Complementary filters
The complementary filter can be thought of as a union of two different filters: a high-pass filter for the gyroscope and a low-pass filter for the accelerometer. The first lets only pass the values ​​above a certain limit, unlike the low-pass filter, which only allows those below.

Accelerometer gives a good indicator of orientation in static conditions and gyroscope gives a good indicator of tilt in dynamic conditions. The formula resulting from combining the two filters is:

angle = (1 - α) * (angle + gyroscope * dt) + α * accelerometer

A common value for α is 0.98, which means that 98% of the weight lays on the gyroscope measurements.

pitch = 0.98 * (pitch + gyroscope_x * dt) + 0.02* accelerometer_x

roll = 0.98 * (roll + gyroscope_y * dt) + 0.02* accelerometer_y

As the data changes very rapidly we can sample for some amount of time and take the average for more precise results.

 using also USING THE MPU6050’S DLPF:

   " using DLPF_CFG 5 , 6 "are the best for cutoff frequency as the Bandwidth (Hz) is 10 and 5 but they have segnificant delay.



