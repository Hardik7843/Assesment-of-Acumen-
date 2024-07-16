from task2_1 import Vehicle

class Car(Vehicle):
    speed_limit = 60
    type_car = ""

    def __init__(self, name , type_car) -> None:
        self.type_car = type_car
        self.name = name
        print(name)

    def car_details(self ):
        print("Details of Bike")
        print( "Name: " + self.name)
        print("Speed: " + self.speed_limit)
        print(self.type_car)


    def start_engine(self):
        print(self.name)
        print("Car Engine started")
        
c1 = Car("C1" , "Maruti Suzuki")
c1.car_details()
# c1.start_engine()
