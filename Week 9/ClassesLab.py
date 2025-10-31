class Monster:
    def __init__(self, _name):
        self.name = _name
        self.size = -1
        self.num_of_teeth = -1
        self.power = -1   
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def set_size(self, value):
        if value > 0:
            self.size = value
    
    def get_num_of_teeth(self):
        return self.num_of_teeth
    
    def set_num_of_teeth(self, value):
        if value >= 0:
            self.num_of_teeth = value
    
    def get_power(self):
        return self.power
    
    def set_power(self, value):
        if value >= 0:
            self.power = value
    
    def scare(self):
        if 80 > self.power > 50:
            return "Very Scary"
        elif self.power < 10:
            return "Cute Monster"
        elif 10 < self.power < 50:
            return "Moderately Scary Monster"
        else:
            return "RUN"
    def __str__(self):
        return f'{self.get_name()} size: {self.get_size()} power: {self.get_power()}. It also has {self.get_num_of_teeth()} teeth so it is {self.scare()}'
    
monster1 = Monster("Krish")
monster1.set_num_of_teeth(30)
monster1.set_power(1)
monster1.set_size(0.1)

print(monster1)
