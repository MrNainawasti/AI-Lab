# Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
# methods start() and stop(). The Car class should have instances of Engine and Wheel classes
# as attributes. Implement a method start_car() in the Car class which starts the engine and prints
# "Car started".

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"Engine of type {self.engine_type} started.")

    def stop(self):
        print("Engine stopped.")


class Wheel:
    def __init__(self, wheel_type):
        self.wheel_type = wheel_type

    def start(self):
        print(f"Wheels of type {self.wheel_type} are ready.")

    def stop(self):
        print("Wheels stopped.")


class Car:
    def __init__(self, engine, wheels):
        self.engine = engine  
        self.wheels = wheels  

    def start_car(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.start()
        print("Car started.\n")

    def stop_car(self):
        for wheel in self.wheels:
            wheel.stop()
        self.engine.stop()
        print("Car stopped.")



# Create an Engine instance
engine = Engine("V8")

# Create Wheel instances
wheels = [Wheel("Alloy")]  

# Create a Car instance
car = Car(engine, wheels)

# Start the car
car.start_car()

# Stop the car
car.stop_car()
