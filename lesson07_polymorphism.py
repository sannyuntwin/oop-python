class TemperatureSensor:
    def read(self):
        print("Temperatrue: 28 degrees Celsius.")
        
class SoilMoistureSensor:
    def read(self):
        print("Soil moisture: 42 percent.")

class LightSensor:
    def read(self):
        print("Light level: 800 lux.")
        
def check_sensor(sensor):
    sensor.read()

sensors = [
    TemperatureSensor(),
    SoilMoistureSensor(),
    LightSensor()
]

for sensor in sensors:
    check_sensor(sensor)