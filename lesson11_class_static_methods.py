class FarmRobot:
    robot_count = 0
    
    def __init__(self, name):
        self.name = name
        FarmRobot.robot_count += 1
        
    @classmethod
    def show_robot_count(cls):
        print(f"Robots created: {cls.robot_count}")
        
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and bool(name.strip())
    
robot1 = FarmRobot("FarmBot-A")
robot2 = FarmRobot("WaterBot")

FarmRobot.show_robot_count()

print(FarmRobot.is_valid_name("HarvestBot"))
print(FarmRobot.is_valid_name("   "))