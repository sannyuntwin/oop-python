class SoilMoistureSensor:
    def read(self):
        return 35
        
class WateringSystem:
    def water(self):
        print("Watering the plants.")
        
class FarmRobot:
    def __init__(self, name, sensor, watering_system):
        self.name = name
        self.sensor = sensor
        self.watering_system = watering_system
        
    def inspect_soil(self):
        moisture = self.sensor.read()
        print(f"Soil  moisture: {moisture}%")
        
        if moisture < 40:
            self.watering_system.water()
        else:
            print("Soil moisture is sufficient.")
        
sensor = SoilMoistureSensor()
watering_system = WateringSystem()

robot = FarmRobot("FarmBot-A", sensor, watering_system)
robot.inspect_soil()