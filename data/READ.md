# AdaptiveSign Dataset

This directory contains sensor data collected from the AdaptiveSign glove.

## Sensor Inputs

Each sample contains 11 sensor features:

- F1–F5: Flex sensor readings
- AX, AY, AZ: Accelerometer readings
- GX, GY, GZ: Gyroscope readings

## Gesture Label

The final column contains the user-defined gesture label.

Example:

```text
F1,F2,F3,F4,F5,AX,AY,AZ,GX,GY,GZ,LABEL
1820,1745,2310,2450,1980,0.42,-0.18,9.63,0.02,-0.01,0.04,HELP
