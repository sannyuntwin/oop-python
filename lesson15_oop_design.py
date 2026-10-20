from abc import ABC, abstractmethod

# Abstraction
class Sensor(ABC):
    @abstractmethod
    def read(self):
        pass

# Inheritance and method implementatin
class TemperatureSensor(Sensor):
    def read(self):
        return 28
    
class SoilMoistureSensor(Sensor):
    def read(self):
        return 35
    
class WateringSystem:
    def water(self):
        print("Watering system activated.")
    

class FarmRobot:
    # Composition: the robot HAS sensors and a waterign system
    def __init__(self, name, sensors, watering_system):
        self.name = name
        self.sensors = sensors
        self.watering_system = watering_system
        
    def inspect_farm(self):
        print(f"{self.name} is inspecting the farm.")
        
        for sensor in self.sensors:
            value = sensor.read()
            print(f"{type(sensor).__name__}: {value}")
            
            if isinstance(sensor, SoilMoistureSensor):
                if value < 40:
                    self.watering_system.water()
                else:
                    print("Soil moisture is sufficent.")
sensors = [
    TemperatureSensor(),
    SoilMoistureSensor()
]    
        
watering_system = WateringSystem()

robot = FarmRobot(
    "FarmRobot-A",
    sensors,
    watering_system
)

robot.inspect_farm()