from ruuvitag_sensor.ruuvi_rx import RuuviTagReactive

ruuvi_rx = RuuviTagReactive()

# Print all notifications
ruuvi_rx.get_subject().\
    subscribe(print)

# Print only last data every 10 seconds for F4:A5:74:89:16:57
ruuvi_rx.get_subject().\
    filter(lambda x: x[0] == 'F4:A5:74:89:16:57').\
    buffer_with_time(10000).\
    subscribe(lambda datas: print(datas[len(datas) - 1]))

# Execute only every time when temperature changes for F4:A5:74:89:16:57
ruuvi_rx.get_subject().\
    filter(lambda x: x[0] == 'F4:A5:74:89:16:57').\
    map(lambda x: x[1]['temperature']).\
    distinct_until_changed().\
    subscribe(lambda x: print('Temperature changed: {}'.format(x)))

# Close all connections and stop bluetooth communication
ruuvi_rx.stop()
