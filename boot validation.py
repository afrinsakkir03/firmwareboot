import serial
import time

# Replace with your Arduino COM port (e.g., "COM3" on Windows, "/dev/ttyUSB0" on Linux)
arduino_port = 'COM11'
baud_rate = 9600
timeout_sec = 5  # Max time to wait for Arduino response

try:
    print(f"Connecting to {arduino_port}...")
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for Arduino to reset and start sending

    print("Waiting for firmware message...")
    start_time = time.time()

    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            print(f"Received: {line}")

            if line == "Firmware version 1.0":
                print("✅ Firmware version validated successfully.")
                break

        if time.time() - start_time > timeout_sec:
            print("❌ Timeout: Firmware version not received.")
            break

    ser.close()

except serial.SerialException as e:
    print(f"Error: Could not open port {arduino_port}.\n{e}")
