from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read(self):
        pass
       
class TemperatureSensor(Sensor): 
    def read(self):
        print("Temperature: 28 degrees Celsius.")

class SoilMoistureSensor(Sensor):  
    def read(self):
        print("Soil moisture: 42 percent.")
        
temperature = TemperatureSensor()
moisture = SoilMoistureSensor()

temperature.read()
moisture.read()

# This world raise TypeError because read() is not implemented:
# sensor = Sensor()