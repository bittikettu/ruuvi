from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

counter = 10
# RunFlag for stopping execution at desired time
run_flag = RunFlag()

def handle_data(found_data):
    print('MAC ' + found_data[0])
    print(found_data[1])
    global counter
    counter = counter - 1
    if counter < 0:
        run_flag.running = False

# List of macs of sensors which will execute callback function
macs = ['EB:F3:38:45:99:59','F6:BA:86:05:C8:29','D9:40:B7:D7:EE:2C','FA:49:B5:0F:F4:60','CB:9F:0F:64:C3:9A','DA:18:E9:BB:2E:6F']

RuuviTagSensor.get_datas(handle_data, macs, run_flag)
