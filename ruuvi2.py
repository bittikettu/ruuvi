import json
from influxdb import InfluxDBClient
import datetime
#from ruuvitag_sensor.ruuvi import RuuviTagSensor
from ruuvitag_sensor.ruuvi_rx import RuuviTagReactive

tagit = {'Takka':'EB:F3:38:45:99:59',
         'Yläkerta':'F6:BA:86:05:C8:29',
         'Sauna':'D9:40:B7:D7:EE:2C',
         'Pesuhuone':'FA:49:B5:0F:F4:60',
         'MhSuihku':'CB:9F:0F:64:C3:9A',
         'Huone1':'DA:18:E9:BB:2E:6F'}

tagit2 = {'EB:F3:38:45:99:59':'Takka',
          'F6:BA:86:05:C8:29':'Yläkerta',
          'D9:40:B7:D7:EE:2C':'Sauna',
          'FA:49:B5:0F:F4:60':'Pesuhuone',
          'CB:9F:0F:64:C3:9A':'MhSuihku',
          'DA:18:E9:BB:2E:6F':'Huone1'}

print(tagit2)
client = InfluxDBClient('192.168.1.87', 8086, 'root', 'root', 'measures')


def handle_data(found_data):
   measurementobj = {}
   json_body = []
   if (found_data[0] in tagit2):
      measurementobj["measurement"] = tagit2[found_data[0]]
      measurementobj["fields"] = found_data[1]
      measurementobj["tags"] = {"sensor": found_data[0]}
      print(json.dumps(measurementobj))
      json_body.append(measurementobj)
      #print(json_body)
      client.write_points(json_body)
    #print('MAC ' + tagit2[found_data[0]])
      #print(found_data[0] in tagit2)
      #print(tagit2[found_data[0]] + " " + str(found_data[1]['temperature']))


interval_in_ms = 5000
RuuviTagSensor.get_datas(handle_data)


