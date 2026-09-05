# ESP32 Smart Glove Pinout

## Microcontroller

ESP32 DevKit

## Flex Sensor Connections

| Sensor | Finger | ESP32 GPIO | Type |
|---|---|---:|---|
| FLEX1 | Thumb | GPIO 34 | Analog Input |
| FLEX2 | Index | GPIO 35 | Analog Input |
| FLEX3 | Middle | GPIO 32 | Analog Input |
| FLEX4 | Ring | GPIO 33 | Analog Input |
| FLEX5 | Little | GPIO 25 | Analog Input |

Each flex sensor is connected as a voltage divider so that finger bending produces a measurable analog voltage.

## MPU6050 Connections

| MPU6050 | ESP32 |
|---|---|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO 21 |
| SCL | GPIO 22 |

## Sensor Data

The ESP32 collects:

- F1–F5: Finger bending measurements
- AX, AY, AZ: Accelerometer measurements
- GX, GY, GZ: Gyroscope measurements

Total sensor features:

**11**

```text
F1 F2 F3 F4 F5
AX AY AZ
GX GY GZ
