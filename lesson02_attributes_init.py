# Attribute store information about each robot
# __init__ initializes an object when it is created

class FarmRobot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        
    def show_status(self):
        print(f"Robot: {self.name}")
        print(f"Battery: {self.battery}%")
        
    robot1 = FarmRobot("FarmBot-A", 100)
    robot2 = FarmRobot("FarmBot-B", 75)
    
    robot1.show_status()
    print("---")
    robot2.show_status