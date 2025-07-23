import serial
import time

def test_firmware_message_not_received_without_reset(port='COM11', baudrate=9600, timeout_sec=10):
    try:
        print(f"🔌 Opening serial port {port} without triggering reset...")

        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        ser.timeout = 1
        ser.open()

        # Disable auto-reset to ensure user reset is required
        ser.setDTR(False)
        ser.setRTS(False)

        print("🧪 TEST CASE 2: Do NOT press the reset button.")
        print(f"⏳ Waiting {timeout_sec} seconds to check for unexpected firmware message...")

        ser.reset_input_buffer()
        start_time = time.time()
        firmware_received = False

        while time.time() - start_time < timeout_sec:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(f"Received: {line}")
                if line == "Firmware version 1.0":
                    firmware_received = True
                    break

        ser.close()

        if firmware_received:
            print("❌ FAIL: Firmware version received without pressing reset.")
        else:
            print("✅ PASS: No firmware message received without reset (expected behavior).")

    except serial.SerialException as e:
        print(f"❌ ERROR: Could not open port {port}.\n{e}")

# Run the test
test_firmware_message_not_received_without_reset()
