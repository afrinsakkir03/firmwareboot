import serial
import time

def test_firmware_not_repeated(port='COM11', baudrate=9600, monitor_duration=15):
    try:
        print(f"🔌 Opening serial port {port} and allowing auto-reset...")
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Allow time for Arduino auto-reset and message

        print(f"🧪 TEST CASE 4: Monitoring for {monitor_duration} seconds after reset")
        print("✔️ Expecting ONLY ONE occurrence of 'Firmware version 1.0'")

        firmware_count = 0
        start_time = time.time()

        while time.time() - start_time < monitor_duration:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    print(f"Received: {line}")
                if line == "Firmware version 1.0":
                    firmware_count += 1

        ser.close()

        if firmware_count == 1:
            print("✅ PASS: Firmware message appeared only once.")
        elif firmware_count == 0:
            print("❌ FAIL: Firmware message did not appear at all.")
        else:
            print(f"❌ FAIL: Firmware message appeared {firmware_count} times.")

    except serial.SerialException as e:
        print(f"❌ ERROR: Could not open port {port}.\n{e}")

# Run the test
test_firmware_not_repeated()
