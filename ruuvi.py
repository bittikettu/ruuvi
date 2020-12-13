import json
from influxdb import InfluxDBClient
import datetime
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

macs = ['EB:F3:38:45:99:59','F6:BA:86:05:C8:29','D9:40:B7:D7:EE:2C','FA:49:B5:0F:F4:60','CB:9F:0F:64:C3:9A','DA:18:E9:BB:2E:6F']

counter = 15
# RunFlag for stopping execution at desired time
run_flag = RunFlag()

tagit = {'Takka':macs[0],
         'Yläkerta':macs[1],
         'Sauna':macs[2],
         'Pesuhuone':macs[3],
         'MhSuihku':macs[4],
         'Huone1':macs[5]}

tagit2 = {macs[0]:'Takka',
          macs[1]:'Yläkerta',
          macs[2]:'Sauna',
          macs[3]:'Pesuhuone',
          macs[4]:'MhSuihku',
          macs[5]:'Huone1'}

print(tagit2)
client = InfluxDBClient('127.0.0.1', 8086, 'root', 'root', 'measures')


def handle_data(found_data):
   measurementobj = {}
   json_body = []
   if (found_data[0] in tagit2):
      print(found_data)
      measurementobj["measurement"] = tagit2[found_data[0]]
      measurementobj["fields"] = found_data[1]
      measurementobj["tags"] = {"sensor": found_data[0]}
      print(json.dumps(measurementobj))
      json_body.append(measurementobj)
      print(json_body)
      client.write_points(json_body)
      global counter
      counter = counter - 1
      if counter < 0:
        run_flag.running = False
    #print('MAC ' + tagit2[found_data[0]])
      #print(found_data[0] in tagit2)
      #print(tagit2[found_data[0]] + " " + str(found_data[1]['temperature']))
RuuviTagSensor.get_datas(handle_data, macs, run_flag)
#RuuviTagSensor.get_datas(handle_data)
