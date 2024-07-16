class Vehicle:
    traffic_light = "Green"

    def __init__(self , name) -> None:
        self.name = name
        print(name)

    
    def start_engine(self):
        print("Engine started")


    
v1 = Vehicle("V1")
v1.start_engine()
