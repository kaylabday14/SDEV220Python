"""
Kayla Day
Module 3 Case Study
This program creates a new object of the user's input of vehicle information for a car.
"""

# Parent class
class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type
    
    def __str__(self):
        return f"{self.vehicle_type}"

# Child class of Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type:str, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors
        self.roof: str = roof

    def __str__(self):

        return (f"Vehicle Type: {super().__str__()}\n" + 
                f"Year: {self.year}\n" +
                f"Make: {self.make}\n" +
                f"Model: {self.model}\n" + 
                f"Doors: {self.doors}\n" + 
                f"Roof: {self.roof}"
        )

# Begins collecting user input
vehicle_type = input('Is your vehicle a truck or car?: ').lower()
vehicle_type.strip()
while vehicle_type != "truck" and vehicle_type!= "car":
    vehicle_type = input('That was not a valid answer, please answer "car" or "truck": ')
vehicle_type.strip()
vehicle_type.capitalize()
while True:
    try:
        year = int(input('Enter the year (xxxx): '))
        if len(str(year)) != 4:
            raise ValueError("Year must be a 4-digit number.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid year.")
make = input('Make: ').capitalize()
make.strip()
model = input('Model: ').capitalize()
model.strip()
while True:
    try:
        doors = int(input('Is it a 2 door or 4 door?: '))
        if doors not in [2, 4]:
            raise ValueError("Doors must be either 2 or 4.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number of doors (2 or 4).")
roof = input('Does it have a solid roof or sunroof?: ').lower()
while roof != "solid" and roof != "sunroof":
    roof = roof.replace(" ", "")
    if roof[:5] == "solid":
        roof = 'Solid'
        break
    elif roof == 'sunroof':
        break
    else:
        roof = input('That is not a valid option. Please enter "solid" or "sunroof": ')
roof.strip()
roof.capitalize()


# Creates instance of car
car = Automobile(
    vehicle_type = vehicle_type,
    year = year,
    make = make,
    model = model,
    doors = doors,
    roof = roof
)

# Print the new object
print(f"New Entry\n---------------------------------------")
print(car)
print('---------------------------------------')