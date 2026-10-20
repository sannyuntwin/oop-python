# A class is a blueprint for creating robot objects.
class FarmRobot:
    def start(self):
        print("Farm robot is starting.")
        
        
    def move(self):
        print("Farm robot is moving through the field")


robot1 = FarmRobot()
robot2 = FarmRobot()

print("---")

robot2.start()
robot2.move()