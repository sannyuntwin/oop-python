class FarmRobot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        
    def move(self, distance):
        print(f"{self.name} moves {distance} meters.")
        self.battery -= distance
        print(f"Battery remaining: {self.battery}%")

robot = FarmRobot("FarmBot-A", 100)

robot.move(10)
robot.move(5)