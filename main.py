class Vehicle(object):
    """Vehicle CLASS"""
    
    def __init__(self):
        super(Vehicle, self).__init__()

        self.name = "Vehicle"
        self.max_speed = 180
        self.mileage = 60000
        
class Bus(Vehicle):
    """Bus CLASS"""
    
    def __init__(self):
        super(Bus, self).__init__()
        
        self.name = "School Volvo"
        
our_100000000_years_old_broken_l_school_bus = Bus()
print(our_100000000_years_old_broken_l_school_bus.name,our_100000000_years_old_broken_l_school_bus.max_speed,our_100000000_years_old_broken_l_school_bus.mileage)

# EXTRA(S)

print(issubclass(Bus, Vehicle)) # returns True
print(issubclass(Vehicle, Bus)) # returns False
