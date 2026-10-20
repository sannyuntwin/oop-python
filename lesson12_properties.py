class FarmRobot:
    def __init__(self, speed):
        self.speed = speed
        
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def  speed(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Speed must be a number.")
        
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        
        self._speed = value
        
robot = FarmRobot(2.5)

print(robot.speed)

robot.speed = 3.0
print(robot.speed)

# Uncommet to test validation:
# robot.speed = =1