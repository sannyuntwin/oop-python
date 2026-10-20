class FarmRobot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        
    def __str__(self):
        return f"{self.name} has {self.battery}% battery."
    
    def __repr__(self):
        return (
            f"FarmRobt(name={self.name!r}, "
            f"battery={self.battery!r})"
        )
        
robot = FarmRobot("FarmBot-A", 85)

print(robot)
print(repr(robot))