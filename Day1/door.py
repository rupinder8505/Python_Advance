class Door:
    color = "Brown"
    def __init__(self,number,status):
        self.number = number
        self.status = status
        self.__name="Test"
    
    def open(self):
        self.status = "open"

    def close(self):
        self.status = "close"

    def get_status(self):
        return self.status


class SecurityDoor(Door):
    def sec_door(self):
        self.sec = True
        return self.sec
        


door1 = Door(10,"open")
print(door1.get_status())

door1.close()
print(door1.get_status())



door2 = SecurityDoor(11,"close")
print(door2.sec_door())
