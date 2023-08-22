#
# MAX30100 test program for MicroPython
#
# Uses library forked from mfitzp/max30100, 
# originally developed for Raspberry Pi
#
# Contact: Rafael Aroca <aroca@ufscar.br>
#

from machine import Pin
from machine import I2C
import max30100
from max30100 import SpO2Calculator
import time

sda=Pin(4)
scl=Pin(5)             
i2c = I2C(scl=scl,sda=sda)

print('Scanning I2C devices...')
print(i2c.scan())

sensor = max30100.MAX30100(i2c=i2c)

print('Reading MAX30100 registers...')
print(sensor.get_registers())

sensor.enable_spo2()

print('Reading sensor...')

for count in range(500):  
  sensor.read_sensor()
  spo2_calculator = SpO2Calculator()
  spo2_calculator.update(sensor.ir, sensor.red, True)
  estimated_spo2 = spo2_calculator.getSpO2()
  
  print(f"Iteration {count + 1}: IR={sensor.ir}, RED={sensor.red}, Estimated SpO2={estimated_spo2}")
  time.sleep(0.5)
