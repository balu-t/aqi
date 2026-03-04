# AQI Simple Reflex Agent

## Overview

This program implements a **Simple Reflex Agent** that determines the **Air Quality Index (AQI)** category based on environmental sensor data.

The agent reads pollution values from a file and classifies the air quality using predefined rules.

This demonstrates the concept of **simple reflex agents in Artificial Intelligence**, where the agent selects actions based only on the **current percept**.

---

## Files Used

### 1. AQI.py

Python program that:

* Reads environmental sensor data
* Calculates the AQI value
* Determines the air quality category

### 2. sensor_data.txt

Contains simulated sensor readings.

Example:

```
PM2.5=45
PM10=80
NO2=30
CO=1.2
```

---

## AQI Classification Rules

| AQI Value | Air Quality Category           |
| --------- | ------------------------------ |
| 0 – 50    | Good                           |
| 51 – 100  | Moderate                       |
| 101 – 150 | Unhealthy for Sensitive Groups |
| 151 – 200 | Unhealthy                      |
| 201 – 300 | Very Unhealthy                 |
| 301+      | Hazardous                      |

---

## How the Program Works

1. The program reads sensor data from `sensor_data.txt`.
2. Pollution values are extracted and converted to numerical values.
3. The AQI value is calculated.
4. The reflex agent compares the AQI value with predefined rules.
5. The corresponding air quality category is displayed.

---

## How to Run

Open a terminal in the project folder and run:

```
python AQI.py
```

or

```
python3 AQI.py
```

---

## Example Output

```
Sensor Data: {'PM2.5': 45.0, 'PM10': 80.0, 'NO2': 30.0, 'CO': 1.2}
Calculated AQI: 39.05
Air Quality: Good
```

---

## Concept Used

Artificial Intelligence – **Simple Reflex Agent**

The agent reacts only to the **current environmental data** without storing previous states.

---

## Author

AI Assignment Submission

