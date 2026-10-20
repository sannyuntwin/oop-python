class FarmRobot:
    farm_name = "Green Vallery Farm" # Shared class attribute
    
    def __init__(self, name):
        self.name = name # Instance attribute
        
robot1 = FarmRobot("FarmBot - A")
robot2 = FarmRobot("FarmBot - B")

print(robot1.name)
print(robot2.name)

print(robot1.farm_name)
print(robot2.farm_name)

FarmRobot.farm_name = "Smart Farm"

print(robot1.farm_name)
print(robot2.farm_name)