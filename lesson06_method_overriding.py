class FarmRobot:
    def work(self):
        print("Robot is working on the farm.")
        
class PlantingRobot(FarmRobot):
    def work(self):
        print("Planting robot is planting seeds.")
        
class HarvestingRobot(FarmRobot):
    def work(self):
        print("Harvesting robot is collecting crops.")
        
robot1 = PlantingRobot()
robot2 = HarvestingRobot()

robot1.work()
robot2.work()