import serial
import csv
import os
import time

# ==========================================
# ESP32 SERIAL SETTINGS
# ==========================================

SERIAL_PORT = "/dev/cu.usbserial-5B150108131"
BAUD_RATE = 115200

# ==========================================
# DATASET SETTINGS
# ==========================================

SAMPLES = 150

FEATURES = [
    "THUMB",
    "INDEX",
    "MIDDLE",
    "RING",
    "LITTLE",
    "AX",
    "AY",
    "AZ",
    "GX",
    "GY",
    "GZ"
]

# Dataset location
DATASET_FILE = "../data/gestures.csv"


# ==========================================
# CONNECT TO ESP32
# ==========================================

print("Connecting to ESP32...")

ser = serial.Serial(
    SERIAL_PORT,
    BAUD_RATE,
    timeout=1
)

time.sleep(2)

print("ESP32 connected!")
print()


# ==========================================
# GET GESTURE LABEL
# ==========================================

gesture = input(
    "Enter gesture name (HELP/YES/NO/WATER/STOP): "
).strip().upper()

print()
print("Gesture selected:", gesture)
print()


# ==========================================
# CREATE DATASET FILE
# ==========================================

file_exists = os.path.exists(DATASET_FILE)

with open(DATASET_FILE, "a", newline="") as file:

    writer = csv.writer(file)

    # Create header if file doesn't exist
    if not file_exists:

        writer.writerow(
            FEATURES + ["LABEL"]
        )

    print("Get ready...")
    time.sleep(2)

    print()
    print("================================")
    print("      DATA COLLECTION")
    print("================================")
    print()

    print("Gesture:", gesture)
    print("Samples:", SAMPLES)
    print()

    input(
        "Press ENTER when you are ready..."
    )

    print()
    print("Starting in 3...")
    time.sleep(1)

    print("2...")
    time.sleep(1)

    print("1...")
    time.sleep(1)

    print()
    print(">>> MAKE THE GESTURE NOW <<<")
    print()

    collected = 0

    while collected < SAMPLES:

        line = ser.readline().decode(
            "utf-8",
            errors="ignore"
        ).strip()

        if not line:
            continue

        # Ignore ESP32 messages
        if not line[0].isdigit() and line[0] != "-":
            continue

        values = line.split(",")

        # We need exactly 11 sensor values
        if len(values) != 11:
            continue

        try:

            # Check that all values are numbers
            [float(x) for x in values]

        except ValueError:
            continue

        # Add gesture label
        row = values + [gesture]

        writer.writerow(row)

        collected += 1

        print(
            f"Collected: {collected}/{SAMPLES}",
            end="\r"
        )

    print()
    print()
    print("================================")
    print("      COLLECTION COMPLETE")
    print("================================")
    print()
    print("Gesture:", gesture)
    print("Samples:", collected)
    print()
    print("Saved to:", DATASET_FILE)


ser.close()
