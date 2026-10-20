class FarmRobot:
    def __init__(self, name, battery):
        self.name = name
        self.__battery = battery
        
    def charge(self, amount):
        if amount <= 0:
            print("Charging amount must be positive.")
            return

        self.__battery = min(100, self.__battery + amount)
        
    def show_battery(self):
        print(f"{self.name} battery: {self.__battery}%")

robot = FarmRobot("FarmBot-A", 60)

robot.show_battery()
robot.charge(25)
robot.show_battery()
robot.charge(-10)