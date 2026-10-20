class Robot:
    def __init__(self, name):
        self.name = name
        
    def start(self):
        print(f"{self.name} is starting.")
        
class WateringRobot(Robot):
    def water_plants(self):
        print(f"{self.name} is watering the plants.")

robot = WateringRobot("WaterRobot")

robot.start()          # Inherited from Robot
robot.water_plants()   # Defined in WateringRobot