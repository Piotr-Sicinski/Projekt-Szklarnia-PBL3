import bme280
import smbus2
from time import sleep
from bluedot.btcomm import BluetoothServer, BluetoothClient
from datetime import datetime, timedelta



def generatePayload(sensorId: int) -> dict:
    
    port = 1
    address = 0x77 # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)
    bme280.load_calibration_params(bus,address)
    
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    #pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    f = open("/sys/bus/iio/devices/iio:device0/in_voltage3_raw", "r")
    
    payload = {
        "sensorId": sensorId,
        "timestamp": str(datetime.now())
    }

    payload["temperature"] = int(humidity)
    payload["humidity"] = int (ambient_temperature)
    payload["moisture"] = int(int(f.read())/264)

    return payload
 
"""
while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    #pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    f = open("/sys/bus/iio/devices/iio:device0/in_voltage3_raw", "r")
    print(int(humidity), int (ambient_temperature),int(int(f.read())/264))
   
    #print (int(f.read())*0.125/330)
    sleep(10)
"""
