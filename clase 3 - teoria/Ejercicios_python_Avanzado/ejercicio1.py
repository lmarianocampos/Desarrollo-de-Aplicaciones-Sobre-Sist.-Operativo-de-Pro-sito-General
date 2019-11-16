from sensor import Sensor,SensorTemp,SensorHum
import time

st0 = SensorTemp(0)
st1 = SensorTemp(1)
st2 = SensorTemp(2)
sh0 = SensorHum(0)
sh1 = SensorHum(1)
print("Valor st0: " + str(st0.get_value()))
print("Valor st1: " + str(st1.get_value()))
print("Valor st2: " + str(st2.get_value()))

print("Valor sh0: " + str(sh0.get_value()))
print("Valor sh1: " + str(sh1.get_value()))

sensorList = []
sensorList.append(SensorTemp(0))
sensorList.append(SensorTemp(1))
sensorList.append(SensorTemp(2))
sensorList.append(SensorHum(0))
sensorList.append(SensorHum(1))
while True:
    time.sleep(0.5)
    Sensor.logFileWrite(sensorList)
