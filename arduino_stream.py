import serial
import time

time.sleep(2)  # wait for Arduino reset
FILEPATH = 'data/arduino/'
FILENAME = 'table_plastic_arduino_950mm'
DURATION = 5  # seconds to record

with serial.Serial('COM5', 115200) as ser, open(FILEPATH + FILENAME + '.csv', 'w') as f:
    start_time = time.time()
    while time.time() - start_time < DURATION:
        line = ser.readline().decode(errors='ignore').strip()
        if line:
            print(line)             # print to terminal
            f.write(line + '\n')    # write to CSV
            f.flush()

print(f"Logging complete: {FILENAME}.csv ({DURATION} seconds)")