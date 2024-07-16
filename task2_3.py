from task2_1 import Vehicle

class Bike(Vehicle):
    speed_limit = 30
    type_bike = ""

    def __init__(self, name , type_bike) -> None:
        self.type_bike = type_bike
        self.name = name
        print(name)

    def bike_details(self ):
        print("Details of Bike")
        print( self.name)
        print( self.speed_limit)
        print( self.type_bike)

    def start_engine(self):
        print(self.name)
        print("Bike Engine started")
        
c1 = Bike("b1" , "Splendor")
c1.bike_details()
# c1.start_engine()